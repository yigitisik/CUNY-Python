from datetime import datetime as dt
import requests
# do this for the first time to make an user account, I already ran the below commented section and
# have an account at  https://pixe.la/@ygtisik
TOKEN = "MCPO2894BFB2SM"
USERNAME = "ygtisik"
endpoint = "https://pixe.la/v1/users"
params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# resp = requests.post(url=endpoint, json=params)
# print(add_pixel_resp.text)
# resp.raise_for_status()

#now we run the graph creation post req
graph_creation_endpoint = f"{endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": "ygtisik-id",
    "name": "ygtisik-disiplin",
    "unit": "commit",
    "type": "float",
    "color": "sora",
    "timezone": "America/New_York",
    "startOnMonday": True,
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# graph_resp = requests.post(url=graph_creation_endpoint, json=graph_params, headers=headers)
# print(graph_resp.text)
# graph_resp.raise_for_status()

#now we do a quick put request to change the color/type of the graph pixels
graph_endpoint = f"{endpoint}/{USERNAME}/graphs/ygtisik-id"
put_params = {
    "color": "ajisai",
    "unit": "commit",
}
# put_resp = requests.put(url=graph_endpoint, json=put_params, headers=headers)
# print(add_pixel_resp.text)
# put_resp.raise_for_status()

#now we do a post request to post a pixel/tile in our graph
pixel_add_params = {
    "date": "20250908",
    "quantity": "6",
}
# add_pixel_resp = requests.post(url=graph_endpoint, json=pixel_add_params, headers=headers)
# print(add_pixel_resp.text)
# add_pixel_resp.raise_for_status()


#can adjust the dateformat to auto-pull for today
today_formatted_date = str(dt.date(dt.today())).replace("-", "")
# OR SIMPLER: dt.now().strftime("%Y%m%d")
# print(today_formatted_date)
# pixel_add_params = {
#     "date": today_formatted_date,
#     "quantity": "15",
# }
# add_pixel_resp = requests.post(url=graph_endpoint, json=pixel_add_params, headers=headers)
# print(add_pixel_resp.text)
# add_pixel_resp.raise_for_status()

# I made two graphs initially so now deleting one with DELETE() req
# keeping ygtisik-id and deleting ygtisikid
# deletion_endpoint = f"{endpoint}/{USERNAME}/graphs/ygtisikid"
# delete_graph_resp = requests.delete(url=deletion_endpoint, headers=headers)
# print(delete_graph_resp.text)


