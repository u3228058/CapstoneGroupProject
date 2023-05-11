import tkinter as tk
from wc_model import *


class WC_GUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tk.Tk()
        self.main_window.title("Wholesale Customer Predictor")

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
        self.title_label = tk.Label(self.one_frame, text='Wholesale Customer Predictor', fg="Blue", font=("Helvetica", 18))
        self.title_label.pack()

        # Create the widgets for Region Options
        self.region_label = tk.Label(self.two_frame, text='Region Of Portugal')
        self.click_region_var = tk.StringVar()
        self.click_region_var.set("Lisbon")
        self.region_inp = tk.OptionMenu(self.two_frame, self.click_region_var, "Lisbon", "Oporto", "Other")
        self.region_label.pack(side='left')
        self.region_inp.pack(side='left')

        # Fresh Products widgets
        self.fresh_label = tk.Label(self.three_frame, text='Fresh:')
        self.fresh_entry = tk.Entry(self.three_frame, bg="white", fg="black", width=10)
        self.fresh_label.pack(side='left')
        self.fresh_entry.pack(side='left')

        # Frozen Products widgets
        self.milk_label = tk.Label(self.four_frame, text='Milk:')
        self.milk_entry = tk.Entry(self.four_frame, bg="white", fg="black", width=10)
        self.milk_label.pack(side='left')
        self.milk_entry.pack(side='left')

        # Grocery Products widgets
        self.grocery_label = tk.Label(self.five_frame, text='Grocery:')
        self.grocery_entry = tk.Entry(self.five_frame, bg="white", fg="black", width=10)
        self.grocery_label.pack(side='left')
        self.grocery_entry.pack(side='left')

        # Frozen Products widgets
        self.frozen_label = tk.Label(self.six_frame, text='Frozen:')
        self.frozen_entry = tk.Entry(self.six_frame, bg="white", fg="black", width=10)
        self.frozen_label.pack(side='left')
        self.frozen_entry.pack(side='left')

        # Detergent & Paper Products widgets
        self.detergentNPapers_label = tk.Label(self.seven_frame, text='Detergent & Paper:')
        self.detergentNPapers_entry = tk.Entry(self.seven_frame, bg="white", fg="black", width=10)
        self.detergentNPapers_label.pack(side='left')
        self.detergentNPapers_entry.pack(side='left')

        # Delicatessen Products widgets
        self.delicatessen_label = tk.Label(self.eight_frame, text='Delicatessen:')
        self.delicatessen_entry = tk.Entry(self.eight_frame, bg="white", fg="black", width=10)
        self.delicatessen_label.pack(side='left')
        self.delicatessen_entry.pack(side='left')

        # Create widgets for prediction of wholesale customer's channel
        self.channel_predict_ta = tk.Text(self.ninth_frame, height=10, width=25, bg='light blue')

        # Create predict button and quit button
        self.button_predict = tk.Button(self.ninth_frame, text='Predict Industry Type Of Wholesale Customer', command=self.predict_channel)
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

    def predict_channel(self):
        result_str = ""
        self.channel_predict_ta.delete(0.0, tk.END)
        customer_Region = self.click_region_var.get()
        if (customer_Region == "Lisbon"):
            customer_Reg = 1;
        elif (customer_Region == "Oporto"):
            customer_Reg = 2;
        else:
            customer_Reg = 3;
        customer_fresh = self.fresh_entry.get()
        customer_milk = self.milk_entry.get()
        customer_grocery = self.grocery_entry.get()
        customer_frozen = self.frozen_entry.get()
        customer_detergentNPapers = self.detergentNPapers_entry.get()
        customer_delicatessen = self.delicatessen_entry.get()
        result_str += "===Customer Information=== \n"
        customer_info = (customer_Reg, customer_fresh, customer_milk, customer_grocery, customer_frozen,
                        customer_detergentNPapers, customer_delicatessen)

        channel_prediction = best_model.predict([customer_info]) #result
        display = ("This prediction has an accuracy of:", str(model_accuracy))

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