import checkUSCIS as api
import send_email as gmail
import config

def main():
    msg = api.requestStatus(config.case_num)
    if msg != config.old_message:
        gmail.send_uscis_update(msg)

if __name__ == "__main__":
    main()
