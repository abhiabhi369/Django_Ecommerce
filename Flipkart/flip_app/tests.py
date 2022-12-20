from django.test import TestCase

import random
import string
import razorpay

client = razorpay.Client(auth=("rzp_test_UHeHgKtMAjdwRc", "ajWJ3rHU0Szz9D2d7DxVnSdL"))

client.payment.capture(paymentId,{
  "amount" : 10,
  "currency" : "INR"
})


