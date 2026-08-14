import imaplib
import email
import io
from PIL import Image
from AppKit import NSPasteboard, NSPasteboardTypePNG, NSImage
from Foundation import NSData

# ---------- CONFIG ----------
IMAP_SERVER = "imap.gmail.com"
EMAIL_USER = "your_email@gmail.com"
EMAIL_PASS = "your_app_password"  # Gmail → App Password needed
SEARCH_SUBJECT = "Images for Clipboard"


# -----------------------------

def copy_image_to_clipboard(img: Image.Image):
    """Copy a PIL image to the macOS clipboard as PNG."""
    # Convert PIL image → PNG bytes
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    png_bytes = buffer.getvalue()
    buffer.close()

    # Convert bytes → NSData
    data = NSData.dataWithBytes_length_(png_bytes, len(png_bytes))

    # Convert NSData → NSImage
    ns_img = NSImage.alloc().initWithData_(data)

    # Put NSImage into the clipboard
    pb = NSPasteboard.generalPasteboard()
    pb.clearContents()
    pb.setData_forType_(ns_img.TIFFRepresentation(), NSPasteboardTypePNG)


def get_image_attachments(msg):
    images = []
    for part in msg.walk():
        if part.get_content_maintype() == "image":
            img_data = part.get_payload(decode=True)
            img = Image.open(io.BytesIO(img_data))
            images.append(img)
    return images


def main():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_USER, EMAIL_PASS)
    mail.select("INBOX")

    status, messages = mail.search(None, f'(SUBJECT "{SEARCH_SUBJECT}")')

    if messages == [b""]:
        print("No matching email found.")
        return

    latest_email_id = messages[0].split()[-1]
    status, msg_data = mail.fetch(latest_email_id, "(RFC822)")

    raw_email = msg_data[0][1]
    msg = email.message_from_bytes(raw_email)

    images = get_image_attachments(msg)

    if not images:
        print("No images found in email.")
        return

    for i, img in enumerate(images, start=1):
        copy_image_to_clipboard(img)
        print(f"✔ Copied image {i} of {len(images)} to macOS clipboard")

if __name__ == "__main__":
    main()
