import gmail
import uscis


def main():
    msg = uscis.requestStatus(uscis.case_num)
    if msg != uscis.old_message:
        gmail.send_strmsg(title="Python: USCIS update", msg=msg)


def handler(event, context):
    main()


if __name__ == "__main__":
    main()
