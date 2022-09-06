import os
import sys

#sys.path.append(f"{os.path.dirname(__file__)}/../../api")
import gmail
import uscis
import json
import copy


def main():
    msg = uscis.requestStatus(uscis.case_num)
    if msg != uscis.old_message:
        gmail.send_strmsg(msg)


if __name__ == "__main__":

    main()
