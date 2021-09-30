import checkUSCIS as api
import send_email as gmail

case_num = "LIN2190249230"
old_message = "On December 14, 2020, we received your Form I-140, Immigrant Petition for Alien Worker, Receipt Number LIN2190249230, and sent you the receipt notice that describes how we will process your case.  Please follow the instructions in the notice.  If you have any questions, contact the USCIS Contact Center at www.uscis.gov/contactcenter.  If you move, go to www.uscis.gov/addresschange to give us your new mailing address."

def main():
    msg = api.requestStatus(case_num)
    if msg != old_message:
        gmail.send_uscis_update(msg)

if __name__ == "__main__":
    main()
