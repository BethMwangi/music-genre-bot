import json
import requests
from django.shortcuts import render
from django.views import generic
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.
class MusicBotView(generic.View):
	def get(self, request, *args, **kwargs):
		if self.request.GET['hub.verify_token'] == '27071345':
			return HttpResponse(self.request.GET['hub.challenge'])
		else:
			return HttpResponse('Error, invalid token')

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)


	# post function to handle Facebook messages
	def post(self, request, *args, **kwargs):
		# converts text payload into a python dictionary 
		incoming_message = json.loads(self.request.body.decode('utf-8'))
		for entry in incoming_message['entry']:
			for message in entry['messaging']:
				if 'message' in message:
					print message
					post_facebook_message(message['sender']['id'],message['message']['text'])

		return HttpResponse()


def post_facebook_message(fbid, received_message):
	post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAADcBC6Vyl0BAPZCJQbZCFDrynzyGEmyVXePs3oviYbwMLStVHZBtRNfmjmhZCgaypxdYrbGPULEon1tJhU35WSmvfhyFji0jwtRcUTDRuKEzWv8obX03ZCBVVZBZC4rjntYYLH8aO6OLTxNfn9haqbDcD56GhiZBZASunfqhi9UGkwZDZD'
	response_msg = json.dumps({"recipient": {"id": fbid}, "message":{"text":received_message}})
	status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=response_msg)
	print status.json()