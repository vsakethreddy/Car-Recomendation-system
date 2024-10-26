from flask import Flask,render_template,request,redirect

from ml import get_recommendations

app=Flask(__name__)



@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        print("post")
        model=request.form['model']
        msrp=request.form['msrp']
        min=0
        max=0
        if(msrp=="10000-20000"):
            min=10000
            max=20000
        if(msrp=="20000-30000"):
            min=20000
            max=30000
        if(msrp=="30000-40000"):
            min=30000
            max=40000
        if(msrp=="40000-50000"):
            min=40000
            max=50000    
        if(msrp=="50000-60000"):
            min=50000
            max=60000
        if(msrp=="60000+"):
            min=60000
            max=100000
        msrp_range = (min, max)  # Specify the MSRP range you want to consider

        # Use the query vector to get recommendations
        recommended_cars = get_recommendations(model,msrp_range)

        print(recommended_cars)

        # print(recommended_cars[0])
        return render_template("show.html",allContacts=recommended_cars)
    return render_template("index.html")



if(__name__=='__main__'):
    app.run(debug=True,port=8000)