import gmail
import uscis

def handler(event, context):
    msg = uscis.requestStatus(uscis.case_num)
    if msg != uscis.old_message:
        gmail.send_strmsg(title="Python: USCIS update", msg=msg)
