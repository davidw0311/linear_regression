from cProfile import run
import numpy as np
import matplotlib.pyplot as plt
import os

def run_linear_regression(show=False):
    demo_imgs = []
    # some target slope and intercept
    target_m = np.random.rand()*20
    target_b = np.random.rand()*10

    # generate random points around the target line
    pointsx = np.linspace(0,5,100)
    pointsy = np.array([target_m*x+target_b+np.random.normal()*4 for x in pointsx])

    # define learning rate and initial parameters
    learning_rate = 0.01
    m = 0
    b = 0
    previous_error = np.sum((pointsy)**2)/len(pointsy)

    print('target m ', target_m, 'target b ', target_b)

    dm = 0.01
    db = 0.01

    if not os.path.exists('saved_imgs'): os.mkdir('saved_imgs')
    # perform linear regression
    for i in range(30):
        
        prediction = np.array([m*x + b for x in pointsx])
        error = np.sum((pointsy-prediction)**2)/len(pointsy)

        prediction_m = np.array([(m+dm)*x + b for x in pointsx])
        prediction_b = np.array([m*x + (b+db) for x in pointsx])
        error_m = np.sum((pointsy-prediction_m)**2)/len(pointsy)
        error_b = np.sum((pointsy-prediction_b)**2)/len(pointsy)
        d_error_dm = (error_m-error)/(dm)
        d_error_db = (error_b-error)/(db)

        
        target_prediction = np.array([target_m*x + target_b for x in pointsx])
        target_error = np.sum((pointsy-target_prediction)**2)/len(pointsy)
        fig = plt.figure()
        plt.clf()
        plt.title('m = '+str(round(m, 3))+'  b='+str(round(b,3))+'  error:'+str(round(error,3))+' target_error: '+str(round(target_error,3)))
        plt.plot(pointsx, prediction, color='red', label='predicted')
        plt.scatter(pointsx, pointsy, color='blue', label='data')
        plt.legend()
        fig.canvas.draw()
        if show:
            plt.show()

        fig.canvas.draw()
        img = np.frombuffer(fig.canvas.tostring_rgb(), np.uint8)
        img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        # img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)


        demo_imgs.append(img)

        m = m - learning_rate*d_error_dm
        b = b - learning_rate*d_error_db

    return demo_imgs

if __name__ == '__main__':
    run_linear_regression(show=True)







