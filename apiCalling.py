# Use 'Requests' package for doing http requests
# 's' in end

# free api website: https://freeapi.hashnode.space/api-guide/apireference/getARandomQuote

# Request ka response json me aata hai, us json response se 
# required i~nfo collect krna bada task hai

import requests

def fetch_random_user():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    
    # get needs a url
    response = requests.get(url)
    # the response generally comes in string or json data
    # converting json to other formats is very easy
    res_data=response.json()   

    # if error while fetching data
    if res_data["success"]==True and "data" in res_data:
        user_info=res_data["data"]
        username=user_info["login"]["username"]
        country=user_info["location"]["country"]

        return username, country
    else:
        raise Exception("failed to fetcht the user data")
    # go to the url and check the req and the response 
    # the response contains "data" as a field

def main():
    try:
        username, country = fetch_random_user()
        print(f'username : {username}, country : {country}')
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()