from flask import Flask, request
from Services.PHYS_273_DE_Solver.DuffingEquationSolver import DuffingEquation as DE
from flask_cors import CORS
import numpy as np
import json

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def homePage():
    return "Hello World"

@app.route('/odeSolver/')
def solveODE():
    
    Xo = float(request.headers.get('Xo'))
    Vo = float(request.headers.get('Vo'))
    to = float(request.headers.get('to'))
    tf = float(request.headers.get('tf'))
    myEquation = DE(alpha=float(request.headers.get('alpha')), 
                    beta=float(request.headers.get('beta')), 
                    delta=float(request.headers.get('delta')), 
                    gamma=float(request.headers.get('gamma')), 
                    omega=float(request.headers.get('omega')))
   
    values = myEquation.ode_solve(to,tf,101,[Xo,Vo]).tolist()
    position = [value[0] for value in values]
    timeList = np.linspace(to, tf, 101).tolist()
    combined = zip(timeList,position)
    data = [{"x": k, "y": v} for (k,v) in combined]
    return json.dumps(data)

app.run()