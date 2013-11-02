__author__ = 'Gerard Whittey'


def get_full_address(data):
    """ This function will concatenating the address1,address2,address3 and
    return the as 1 string
    """
    mydata = data.addressseq.streetno + ' ' + data.addressseq.address1 + ' '
    mydata = mydata + data.addressseq.address2 + ' ' + data.addressseq.address3
    return mydata

