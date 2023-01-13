import time
from plyer import notification
from datetime import datetime
class_no=0
if __name__=="__main__":
    while(True):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        current_day = now.strftime("%a")
        #Monday schedule
        if current_day=="Mon":
            if current_time=="12:55":
                notification.notify(
                    title="CHE110 (Environmental)",
                    message="Room: 37-610",
                    timeout=17,
                )
                class_no+=1
            if current_time=="13:55":
                notification.notify(
                    title="ECE:249 (Basic Electrical and Electronics)",
                    message="Room: 37-806",
                    timeout=17,
                )
                class_no+=1
            if current_time=="14:55":
                notification.notify(
                    title="CSE326 (HTML and CSS)",
                    message="Room: 26-502",
                    timeout=17,
                )
                class_no+=1
            if current_time=="15:55":
                notification.notify(
                    title="CSE326 (HTML and CSS)",
                    message="Room: 26-502",
                    timeout=17,
                )
                class_no+=1
            if class_no==4:
                time.sleep(16*60*60)
        #Tuesday schedule
        if current_day=="Tue":
            if current_time=="12:55":
                notification.notify(
                    title="CHE110 (Environmental)",
                    message="Room: 37-610",
                    timeout=17,
                )
                class_no+=1
            if current_time=="13:55":
                notification.notify(
                    title="ECE:249 (Basic Electrical and Electronics)",
                    message="Room: 37-806",
                    timeout=17,
                )
                class_no+=1
            if current_time=="14:55":
                notification.notify(
                    title="CSE326 (HTML and CSS)",
                    message="Room: 26-502",
                    timeout=17,
                )
                class_no+=1
            if current_time=="15:55":
                notification.notify(
                    title="CSE326 (HTML and CSS)",
                    message="Room: 26-502",
                    timeout=17,
                )
                class_no+=1
            if class_no==4:
                time.sleep(16*60*60)
        #Wednesday schedule
        if current_day=="Wed":
            if current_time=="12:55":
                notification.notify(
                    title="CHE110 (Environmental)",
                    message="Room: 37-610",
                    timeout=17,
                )
                class_no+=1
            if current_time=="13:55":
                notification.notify(
                    title="ECE:249 (Basic Electrical and Electronics)",
                    message="Room: 37-806",
                    timeout=17,
                )
                class_no+=1
            if current_time=="14:55":
                notification.notify(
                    title="CSE326 (HTML and CSS)",
                    message="Room: 26-502",
                    timeout=17,
                )
                class_no+=1
            if current_time=="15:55":
                notification.notify(
                    title="CSE326 (HTML and CSS)",
                    message="Room: 26-502",
                    timeout=17,
                )
                class_no+=1
            if class_no==4:
                time.sleep(16*60*60)
        #Thursday schedule
        if current_day=="Thu":
            if current_time=="12:55":
                notification.notify(
                    title="CHE110 (Environmental)",
                    message="Room: 37-610",
                    timeout=17,
                )
                class_no+=1
            if current_time=="13:55":
                notification.notify(
                    title="ECE:249 (Basic Electrical and Electronics)",
                    message="Room: 37-806",
                    timeout=17,
                )
                class_no+=1
            if current_time=="14:55":
                notification.notify(
                    title="CSE326 (HTML and CSS)",
                    message="Room: 26-502",
                    timeout=17,
                )
                class_no+=1
            if current_time=="15:55":
                notification.notify(
                    title="CSE326 (HTML and CSS)",
                    message="Room: 26-502",
                    timeout=17,
                )
                class_no+=1
            if class_no==4:
                time.sleep(16*60*60)
        #Friday schedule
        if current_day=="Fri":
            if current_time=="12:55":
                notification.notify(
                    title="CHE110 (Environmental)",
                    message="Room: 37-610",
                    timeout=17,
                )
                class_no+=1
            if current_time=="13:55":
                notification.notify(
                    title="ECE:249 (Basic Electrical and Electronics)",
                    message="Room: 37-806",
                    timeout=17,
                )
                class_no+=1
            if current_time=="14:55":
                notification.notify(
                    title="CSE326 (HTML and CSS)",
                    message="Room: 26-502",
                    timeout=17,
                )
                class_no+=1
            if current_time=="15:55":
                notification.notify(
                    title="CSE326 (HTML and CSS)",
                    message="Room: 26-502",
                    timeout=17,
                )
                class_no+=1
            if class_no==4:
                time.sleep(16*60*60)
            