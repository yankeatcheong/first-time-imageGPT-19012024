from flask import Flask,request,render_template
import json,requests,time
headers = {
    "Authorization" : "Token r8_ZpjqDrwkFx4PK9Qn7Rz0WIblxUA0Gd64Y5mIm ",
    "Content-Type" : "application/json"
}
app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        q = request.form.get("q")
        print(q)
        data = json.dumps(
            {
                "version" : "db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
                "input" : {"prompt":q}
            }
        )
        r = requests.post("https://api.replicate.com/v1/predictions",data=data,headers=headers)
        time.sleep(10)
        r = r.json()["urls"]['get']
        r = requests.post(r,headers=headers).json()["output"]
        return(render_template("index.html",result=r[0]))
    else:
        return(render_template("index.html",result="waiting for rate to enter ........"))
if __name__ == "__main__":
    app.run()
