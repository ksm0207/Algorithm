import requests
from reddit import call_reddit
from flask import Flask, render_template, request

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""
app = Flask("DayEleven")

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
}


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django",
]


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/read")
def read():
    check_select = []
    return_data = []

    for i in subreddits:
        check = request.args.get(i)
        print(check)
        if check == "on":
            check_select.append(i)

    for language in check_select:
        print("Check_select = ", language)

        url = f"https://www.reddit.com/r/{language}/top/?t=month"
        data = call_reddit(url, language)
        return_data.append(data)

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", return_data)
    print(check_select)
    return render_template(
        "read.html", return_data=return_data, check_select=check_select
    )


app.run(debug=True)
