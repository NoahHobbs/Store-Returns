"""
Noah Hobbs
11/12/2020
Kohls/Amazon return program with GUI
"""
import PySimpleGUI as sg


class ItemReturn:
    # Item return is acting like my node class for a linked list
    def __init__(self, items, company):
        self.items = items  # items to be returned
        self.company = company  # name of the company that the return is from
        self.nxt = None  # used to get the next item in the queue
        self.size = len(self.items)  # size of the returns


class ReturnQueue:
    def __init__(self):
        self.queue_size = 0  # the size of the queue
        self.amazon_front = None  # front of the amazon returns
        self.kohls_front = None  # front of the kohls returns

    def make_return(self, item_return):
        """
        Basically is my enqueue method
        :param item_return: the item to be enqueued
        :return: no return but the method increments the queue size and
        enqueues what item is passed
        """
        company = "amazon" if item_return.company.lower() == "amazon" else \
            "kohls"
        front = getattr(self, f'{company}_front')
        if front is None:
            setattr(self, f'{company}_front', item_return)
        else:
            setattr(self, f'{company}_front',
                    self.set_front(front, item_return))
        self.queue_size += 1

    def set_front(self, one, two):
        """
        Sets the front of my queue
        """
        if one is None:
            return two
        if two is None:
            return one
        temp = None
        if len(one.items) < len(two.items):
            temp = one
            one.nxt = self.set_front(one.nxt, two)
        else:
            temp = two
            two.nxt = self.set_front(one, two.nxt)
        return temp

    def return_all(self, company=None):
        """
        :param company: If the user passes a company it will return the
        returns of that company (Used heavily in the GUI implementation)
        :return: Returns all the items that have been enqueued
        """
        if not company:
            kohls_return = self.return_all("kohls")
            amazon_return = self.return_all("amazon")
            return kohls_return + amazon_return
        my_list = []
        company = "amazon" if company.lower() == "amazon" else "kohls"
        while getattr(self, f'{company}_front'):
            my_list.append(self.next_return(company))
        return my_list

    def next_return(self, company=None):
        """
        Gets the next item in the queue
        :param company: Either amazon or kohls
        :return: returns the current front of the queue
        """
        if not company:
            kohls_return = self.next_return("kohls")
            amazon_return = self.next_return("amazon")
            return [kohls_return, amazon_return]
        company = "amazon" if company.lower() == "amazon" else "kohls"
        front = getattr(self, f'{company}_front')
        curr = front
        nx = getattr(self, f'{company}_front').nxt
        curr.nxt = None
        setattr(self, f'{company}_front', nx)
        return curr.items

    def amt_of_returns(self):
        # this method was mainly for testing because the attributes take the
        # place of it later in the program
        # I left it just to give an idea of how the program morphed over time
        return f'{self.queue_size} Customers have made returns'


if __name__ == '__main__':
    # making my return queue object
    return_queue = ReturnQueue()
    # Creating my Theme
    sg.theme('Topanga')
    # Creating my layout
    layout = [[sg.Text('Enter your returns (Separate values by comma)')],
              [sg.InputText(key="returned")],
              [sg.Radio('Kohl\'s', "RADIO1", default=False, key="kohls")],
              [sg.Radio(
                  'Amazon', "RADIO1", default=False, key="amazon",)],
              [sg.Button('Enter')],
              [sg.Text('Amazon to process'), sg.Text('Kohl\'s to process')],
              [sg.Text('', key='amazon_text', size=(16, 12)),
               sg.Text('', key='kohls_text', size=(10, 12))],
              [sg.Button('Process all'), sg.Button('Process Kohl\'s',
                                                   key="return_kohls"),
              sg.Button('Process Amazon', key="return_amazon")],
              [sg.Button('Exit')]]

    # Create the Window
    window = sg.Window('Returns', layout, size=(300, 350))
    # reads the user events or if the user closes
    while True:

        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':  # if the user closes
            # the window
            break
        # if the user enters their returns get the company that they select
        # and update the text box to be empty
        if event == 'Enter':
            if values['returned'] == '' or values['returned'] == ' ':
                sg.Popup('Please make at least one return', title='ERROR')
                continue

            if values["kohls"]:
                # setting the company to Kohls if the radio button is selected
                company = "Kohls"
                set_window = window.FindElement('kohls_text')
                # this line ensures that I won't have the list of returns and
                # with the text showing how many returns were made
                if 'process' in set_window.get():
                    set_window.Update('')

                set_window.Update(f'{set_window.get()}\n{values["returned"]}')

            else:
                # setting the company to Amazon if the radio button is selected
                company = "Amazon"
                set_window = window.FindElement('amazon_text')
                # this line ensures that I won't have the list of returns and
                # with the text showing how many returns were made
                if 'process' in set_window.get():
                    set_window.Update('')
                set_window.Update(f'{set_window.get()}\n{values["returned"]}')

            # change variable after deleting other main
            my_item4 = ItemReturn(values["returned"].split(','), company)
            return_queue.make_return(my_item4)
            print(f'You entered {values["returned"]}')
            # clearing my text field after the user enters a return
            window.FindElement('returned').Update('')
        if event == 'Return all':
            # will return both Kohl's and Amazon returns regardless of their
            # company
            print(return_queue.return_all())
            window.FindElement('kohls_text').Update(f'All Kohl\'s returns '
                                                    'processed')
            window.FindElement('amazon_text').Update('All Amazon returns '
                                                     'processed')
        if event == "return_kohls":
            # Returns specifically Kohl's items
            x = return_queue.return_all("Kohls")
            total_num_returns = sum([len(r) for r in x])
            window.FindElement('kohls_text').Update(f'{total_num_returns} '
                                                    f'Kohl\'s returns '
                                                    'processed')
        if event == "return_amazon":
            # Returns specifically Amazon items
            x = return_queue.return_all("Amazon")
            total_num_returns = sum([len(r) for r in x])
            window.FindElement('amazon_text').Update(f'{total_num_returns} '
                                                     f'Amazon returns '
                                                     'processed')
        # this line resolved some issues with the GUI I was having
        window.Refresh()
    # closing my window
    window.close()
    # once the user exits the GUI this line executes
    input('Press any key to continue')
