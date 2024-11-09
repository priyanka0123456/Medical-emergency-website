import streamlit as st
from twilio.rest import Client 

def make_call_and_send_message():
    account_sid = 'ACcfb5e3785c01f26b1b1f6ac8292f2fa4'
    auth_token = 'b5916ae9cecdcc37b19aa38ffa41c898'
    client = Client(account_sid, auth_token)    
    to_number = '+917095778481'
    from_number = '+12134189125'
    
    # Make a call
    call = client.calls.create(
                        twiml='<Response><Say>Emergency , Patient : Srikar , Age : 22 , Health condition : Critical , Location : road number 3 </Say></Response>',
                        to=to_number,
                        from_=from_number
    )
    st.success("Call SID: " + call.sid)
    
    # Send a message
    message = client.messages.create(
        to="+917095778481",
        from_="12134189125",
        body="Emergency - Patient : Srikar , Age : 22 , Health condition : Critical , Location : road number 3"
    )
    st.success("Message SID: " + message.sid)

def main():
    st.title("Emergency Alert System")
    st.write("Click the button below to send an emergency alert call and message.")
    
    if st.button("Send Emergency Alert"):
        make_call_and_send_message()

if __name__ == "__main__":
    main()