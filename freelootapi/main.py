from flask import Flask, redirect, url_for, render_template
import json
import requests
import webbrowser

app = Flask(__name__)

@app.route("/index.html")
def home():
    r=requests.get("https://api.clashroyale.com/v1/clans/%23PP289R82", headers={"Accept":"application/json", "authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjEwZjYzYzBjLTA0NzItNDc1My1hZGI1LTE2OTkyNmFiYmFiMiIsImlhdCI6MTY2NTA1NDU5NCwic3ViIjoiZGV2ZWxvcGVyLzk3ZTAzYzA3LTI5ZDUtODMyMS0wYjg5LTEyZjQ5Zjg2NmU1ZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNzMuMTcuMjI0LjE4MiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.bQ4G1RruoDeOovpqwodTprNEKR416XFCQVY7DKwCxpr5fDkd4EOsa59OpX7xuW7A0_GZnFz6DWWgZCI5Cj5_6w"})
    clan_data=json.dumps(r.json(), indent = 4)
    return render_template("index.html", clan_data=clan_data)

@app.route("/riverrace.html")
def riverrace():
    r=requests.get("https://api.clashroyale.com/v1/clans/%23PP289R82/riverracelog", headers={"Accept":"application/json", "authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjEwZjYzYzBjLTA0NzItNDc1My1hZGI1LTE2OTkyNmFiYmFiMiIsImlhdCI6MTY2NTA1NDU5NCwic3ViIjoiZGV2ZWxvcGVyLzk3ZTAzYzA3LTI5ZDUtODMyMS0wYjg5LTEyZjQ5Zjg2NmU1ZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNzMuMTcuMjI0LjE4MiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.bQ4G1RruoDeOovpqwodTprNEKR416XFCQVY7DKwCxpr5fDkd4EOsa59OpX7xuW7A0_GZnFz6DWWgZCI5Cj5_6w"})
    river_data=json.dumps(r.json(), indent = 4)
    return render_template("riverrace.html", river_data=river_data)

@app.route("/players.html")
def players():
    r=requests.get("https://api.clashroyale.com/v1/clans/%23PP289R82/members", headers={"Accept":"application/json", "authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjEwZjYzYzBjLTA0NzItNDc1My1hZGI1LTE2OTkyNmFiYmFiMiIsImlhdCI6MTY2NTA1NDU5NCwic3ViIjoiZGV2ZWxvcGVyLzk3ZTAzYzA3LTI5ZDUtODMyMS0wYjg5LTEyZjQ5Zjg2NmU1ZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNzMuMTcuMjI0LjE4MiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.bQ4G1RruoDeOovpqwodTprNEKR416XFCQVY7DKwCxpr5fDkd4EOsa59OpX7xuW7A0_GZnFz6DWWgZCI5Cj5_6w"})
    clan_members=json.dumps(r.json(), indent = 4)
    return render_template("players.html", clan_members=clan_members)

@app.route("/github.html")
def github(): 
    webbrowser.open('http://github.com')

if __name__ == "__main__":
    app.run(debug=True)