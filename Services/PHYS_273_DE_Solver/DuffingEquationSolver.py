import numpy as np
from scipy.integrate import odeint
class DuffingEquation:
    
    def __init__(self, alpha, beta, delta, gamma, omega):
        self.alpha = alpha
        self.beta = beta
        self.delta = delta
        self.gamma = gamma
        self.omega = omega
        
        def DuffingEquation(x_vector, t, alpha, beta, delta, gamma, omega):
            x,v = x_vector
            dydt = [v, -delta*v - alpha*x - beta*x**3 + gamma*np.cos(omega*t)]
            return dydt
        
        self.DuffingEquation = DuffingEquation
    
    #Returns an array of vectors that contain position and velocity
    #Initial position must be a 2d vector
    def ode_solve(self, initialTime, finalTime, numTimeSteps, initialPosition):
        t = np.linspace(initialTime, finalTime, numTimeSteps)
        sol = odeint(self.DuffingEquation,initialPosition, t, args=(self.alpha, self.beta, self.delta, self.gamma, self.omega))
        return sol
    
    def getTimeList(initialTime, finalTime, numTimeSteps):
        return np.linspace(initialTime, finalTime, numTimeSteps)
    
    def setAlpha(self, alpha):
        self.alpha = alpha
        
    def setBeta(self, beta):
        self.beta = beta

    def setDelta(self, delta):
        self.delta = delta

    def setGamma(self, gamma):
        self.gamma = gamma

    def setOmega(self, omega):
        self.omega = omega