import gmail
import uscis


def main():
    msg = uscis.requestStatus(uscis.case_num)
    if msg != uscis.old_message:
        gmail.send_strmsg(title="Python: USCIS update", msg=msg)
    return msg


def handler(event, context):
    msg = main()

    if event["key1"] == "test":
        gmail.send_strmsg(title="Python: USCIS update: test", msg=msg)


if __name__ == "__main__":
    main()
