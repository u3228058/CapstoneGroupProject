import tkinter as tk
from de_model import best_model

class DE_GUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tk.Tk()
        self.main_window.title("MMI predictor")

        # Create widgets.
        self.one_frame = tk.Frame()
        self.two_frame = tk.Frame()
        self.three_frame = tk.Frame()
        self.four_frame = tk.Frame()

        # Create title display
        self.title_label = tk.Label(self.one_frame, text='MMI predictor', fg="Blue", font=("Helvetica", 18))
        self.title_label.pack()

        self.magnitude_label = tk.Label(self.two_frame, text='Magnitude:')
        self.magnitude_entry = tk.Entry(self.two_frame, bg="white", fg="black", width=12)
        self.magnitude_label.pack(side='left')
        self.magnitude_entry.pack(side='left')

        self.depth_label = tk.Label(self.three_frame, text='Depth (km):')
        self.depth_entry = tk.Entry(self.three_frame, bg="white", fg="black", width=10)
        self.depth_label.pack(side='left')
        self.depth_entry.pack(side='left')

        self.magnitude_predict_ta = tk.Text(self.four_frame, height=10, width=25, bg='light blue')

        self.button_predict = tk.Button(self.four_frame, text='Predict MMI', command=self.predict_MMI)
        self.button_quit = tk.Button(self.four_frame, text='Quit', command=self.main_window.destroy)

        self.magnitude_predict_ta.pack(side='left')
        self.button_predict.pack()
        self.button_quit.pack()

        self.one_frame.pack()
        self.two_frame.pack()
        self.three_frame.pack()


        tk.mainloop()

    def predict_MMI(self):
        result_str = ""
        self.magnitude_predict_ta.delete('1.0', tk.END)

        earthquake_magnitude = self.magnitude_entry.get()
        earthquake_depth = self.depth_entry.get()

        result_str += "=== Earthquake MMI ===\n"
        earthquake_MMI = (earthquake_magnitude, earthquake_depth)

        earthquake_prediction = best_model.predict([earthquake_MMI])
        display = f"This earthquake has an MMI of: {earthquake_prediction}"
        result_str = display

        if earthquake_prediction == 0:
            result_str += "\n0 - No damage"
        elif earthquake_prediction == 1:
            result_str += "\n1 - Minor damage"
        elif earthquake_prediction == 2:
            result_str += "\n2 - Moderate damage"
        elif earthquake_prediction == 3:
            result_str += "\n3 - Strong damage"
        elif earthquake_prediction == 4:
            result_str += "\n4 - Severe damage"
        elif earthquake_prediction == 5:
            result_str += "\n5 - Devastating damage"
        else:
            result_str += "\nInvalid prediction"

        self.magnitude_predict_ta.insert('1.0', result_str)


def test1():
    earthquake_info = (7.5, 10)
    assert best_model.predict([earthquake_info]) == 4

def test2():
    earthquake_info = (6.2, 5)
    assert best_model.predict([earthquake_info]) == 2

test1()
test2()
print("Test 1 & 2 passed")

my_wde_GUI = DE_GUI()

