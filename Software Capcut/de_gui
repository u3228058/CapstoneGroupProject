import tkinter as tk
from wc_model import *


class WC_GUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tk.Tk()
        self.main_window.title("MMI predictor")

        # Create widgets.
        self.one_frame = tk.Frame()
        self.two_frame = tk.Frame()
        self.three_frame = tk.Frame()
        self.four_frame = tk.Frame()
        self.five_frame = tk.Frame()
        self.six_frame = tk.Frame()
        self.seven_frame = tk.Frame()
        self.eight_frame = tk.Frame()
        self.ninth_frame = tk.Frame()

        # Create title display
        self.title_label = tk.Label(self.one_frame, text='MMI predictor', fg="Blue", font=("Helvetica", 18))
        self.title_label.pack()
        

        self.magnitude_label = tk.Label(self.three_frame, text='Magnitude:')
        self.magnitude_entry = tk.Entry(self.three_frame, bg="white", fg="black", width=12)
        self.magnitude_label.pack(side='left')
        self.magnitude_entry.pack(side='left')

    
        self.depth_label = tk.Label(self.four_frame, text='Depth:')
        self.depth_entry = tk.Entry(self.four_frame, bg="white", fg="black", width=10)
        self.depth_label.pack(side='left')
        self.depth_entry.pack(side='left')

      
         self.magnitude_predict_ta. = tk.Text(self.ninth_frame, height=10, width=25, bg='light blue')

       
        self.button_predict = tk.Button(self.ninth_frame, text='Predicate MMI', command=self.predict_Predicate_MMI)
        self.button_quit = tk.Button(self.ninth_frame, text='Quit', command=self.main_window.destroy)

        self.channel_predict_ta.pack(side='left')
        self.button_predict.pack()
        self.button_quit.pack()

        self.one_frame.pack()
        self.two_frame.pack()
        self.three_frame.pack()
        self.four_frame.pack()
        self.five_frame.pack()
        self.six_frame.pack()
        self.seven_frame.pack()
        self.eight_frame.pack()
        self.ninth_frame.pack()

        tk.mainloop()

    def predict_Predicate_MMI(self)\:7
        result_str = ""
        self.magnitude_predict_ta.delete(0.0, tk.END)
      
            customer_Reg = 3;
        earthquake_magnitude = self.magnitude_entry.get()
        earthquake_depth = self.depth_entry.get()
       
        result_str += "===Earthquake MMI=== \n"
        earthquake_MMI = (earthquake_magnitude,earthquake_depth)

        earthquake_prediction = best_model.predict([MMI]) #result
        display = ("This earthquake has an MMI of:", str(model_accuracy))

        if (channel_prediction == [0]):
            result_str = (display, '\n', "0 - Customer should be in Hospitality Industry")
        else:
            result_str = (display, '\n' + "1 - Customer should be in retail Industry")
        self.channel_predict_ta.insert('1.0', result_str)

    #Testing
    def test1():
        customer_info = (2, 304, 135, 127, 87, 215, 77)
        assert best_model.predict([customer_info]) == 0

    def test2():
        customer_info = (2, 158, 393, 414, 263, 402, 102)
        assert best_model.predict([customer_info]) == 1

    test1()
    test2()
    print("Test 1 & 2 passed")
my_wc_GUI = WC_GUI()
