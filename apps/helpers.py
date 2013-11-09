__author__ = 'Gerard Whittey'


def get_full_address(data):
    """ This function will concatenating the address1,address2,address3 and
    return the as 1 string
    """
    mydata = data.addressseq.streetno + ' ' + data.addressseq.address1 + ' '
    mydata = mydata + data.addressseq.address2 + ' ' + data.addressseq.address3
    return mydata


def write_error(error_file, err_name, id):
    my_error_file = 'logs/%s' % error_file
    err = open(my_error_file, 'a')
    err.write(str(id) + ',' + err_name + '\n')


def get_or_none(cls, **cond):
    try:
        return cls.objects.get(**cond)
    except cls.DoesNotExist:
        return None


def find_title(title):
    if title == 1:
        title = "Mr."
    elif title == 2:
        title = "Dr."
    elif title == 4:
        title = "Ms."
    elif title == "8":
        title = "Miss."
    else:
        title = "NO TITLE"
    return title