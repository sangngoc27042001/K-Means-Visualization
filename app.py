from flask import Flask, render_template, request
from KM import *
from werkzeug.utils import redirect
Score_alphabet =0
BScore_alphabet =0
app = Flask(__name__,template_folder="templates")
client_num=-1

@app.route('/')
def home():
    global client_num
    if client_num==9:
        client_num=0
    else:
        client_num+=1
    return render_template('KM_index.html',hh="heading",client_num=client_num)

@app.route('/KM_draw', methods=['GET', 'POST'])
def KM_draw():
    cn=int(request.form['client_num'])
    try:
        data= to2Darray(request.form['datapoint'])
        if(len(data)==0):
            return redirect("/")
        K=request.form['K']
        print((K,cn))
        kmeans_array[cn].set_init(int(K), data)
    except:
        pass
    
    ret=kmeans_array[cn].points_with_centroids()
    print(ret)
    try:
        if(request.form['clear']=="yes"):
            return redirect("/")
        if(request.form['random']=="yes"):
            kmeans_array[cn].random()
        else:
            kmeans_array[cn].step()
    except:
        pass
    ret=kmeans_array[cn].points_with_centroids()
    return render_template(
        'KM_step.html',hh="heading", 
        inn=ret[0], 
        centroid=ret[1],
        client_num=cn
        )

if __name__ == '__main__':
    app.run(debug=True)