class User:
    def __init__(
        self, firstName, lastName, address, accountNumber, ratePlan, *args, **k
    ) -> None:
        self.first_name = firstName
        self.last_name = lastName
        self.address = address
        self.plan = ratePlan
        self.account_number = accountNumber

    def __repr__(self) -> str:
        return f"<User({self.account_number},{self.first_name},{self.last_name})>"


class RechargeResponse:
    def __init__(self, data):
        if data.get("rechargeResponse") != None:
            if data["rechargeResponse"]["status"] == "true":
                self.status = True
            else:
                self.status = False
            self.requestId = data["rechargeResponse"]["requestId"]
        else:
            raise ("An expected error in server response : " + data)


class SendVerificationCodeResponse:
    def __init__(self, status, verCodeDuration, **kwargs) -> None:
        self.status = status
        self.duration = verCodeDuration
        self.errorCode = None
        self.message = None
        if "fault" in kwargs.keys():
            data = kwargs["fault"]
            self.errorCode = data["errorCode"]
            self.message = data["message"]
            self.userMessageEn = data["userMessageEn"]
            self.userMessageAr = data["userMessageAr"]

    def __repr__(self) -> str:
        return f"<Response(IsSuccess:{self.status},errorCode:{self.errorCode},message:{self.message})>"


class SubmitResponse:
    def __init__(self, data):
        if data.get("submitResponse") != None:
            if data["submitResponse"]["status"] == "true":
                self.status = True
            else:
                self.status = False
            self.orderId = data["submitResponse"]["orderId"]
        else:
            raise ("An expected error in server response : " + data)

    def __repr__(self) -> str:
        return f"<SubmitResponse(IsSuccess:{self.status},OrderId:{self.orderId})>"


class Gift:
    def __init__(self, gift_units, gift_number, is_redeemed, is_today_gift):
        self.value = gift_units
        self.day = gift_number
        self.today_gift = is_today_gift
        if is_redeemed == "FALSE":
            self.redeemed = False
        else:
            self.redeemed = True
        if is_today_gift == "FALSE":
            self.today_gift = False
        else:
            self.today_gift = True

    def __str__(self):
        return f"Gift(Value={self.value},Day = {self.day} ,Today's Gift ? = {self.today_gift})"


class Constants:
    application_password = "ZFZyqUpqeO9TMhXg4R/9qs0Igwg="
    build_number = "547"
    app_version = "22.13.0"
    device_name = "Iphone 13 pro"
    API_ENDPOINT = "https://mab.etisalat.com.eg:11003"
