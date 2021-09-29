from flask import Flask, render_template, request
from KM import *
from werkzeug.utils import redirect
Score_alphabet =0
BScore_alphabet =0
app = Flask(__name__,template_folder="templates")
data=np.array([])
client_num=-1

@app.route('/')
def home():
    global client_num
    if client_num==9:
        client_num=0
    else:
        client_num+=1
    return render_template('KM_index.html',hh="heading", inn=data.tolist(),client_num=client_num)

@app.route('/KM_step', methods=['GET', 'POST'])
def KM_step():
    data= to2Darray(request.form['datapoint'])
    for i in data:
        print(i)
    if(len(data)==0):
        return redirect("/")
    K=request.form['K']
    cn=int(request.form['client_num'])
    print((K,cn))
    kmeans_array[cn].set_init(int(K), data)
    ret=kmeans_array[cn].points_with_centroids()
    print(ret)
    return render_template(
        'KM_step.html',hh="heading", 
        inn=ret[0], 
        centroid=ret[1],
        client_num=cn
        )

@app.route('/KM_draw', methods=['GET', 'POST'])
def KM_draw():
    cn=int(request.form['client_num'])
    if(request.form['clear']=="yes"):
        return redirect("/")
    if(request.form['random']=="yes"):
        kmeans_array[cn].random()
    else:
        kmeans_array[cn].step()
    ret=kmeans_array[cn].points_with_centroids()
    return render_template(
        'KM_step.html',hh="heading", 
        inn=ret[0], 
        centroid=ret[1],
        client_num=cn
        )

if __name__ == '__main__':
    app.run(debug=True)