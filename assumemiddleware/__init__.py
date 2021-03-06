from django.contrib.auth import get_user_model
from django.shortcuts import redirect

class AssumeMiddleware(object):
	"""If enabled, each request object will have it's user attribute set to the assumed user.

	The following additional attributes will also be added to the request.user object:
	user.from_user - the actual logged in staff user
	user.is_assumed - True when the user is assumed
	"""

	def process_request(self, request):
		assume = request.GET.get('assume', None)
		unassume = request.GET.get('unassume', None)

		if assume:
			request.session['assume_username'] = assume
			if request.META.has_key('HTTP_REFERER') and request.META['HTTP_REFERER']:
				request.session['assume_referer'] = request.META['HTTP_REFERER']

		if not unassume and request.session.has_key('assume_username') and request.user.is_staff:
			try:
				from_user = request.user
				request.user = get_user_model().objects.get(username=request.session['assume_username'])
				request.user.is_assumed = True
				request.user.from_user = from_user
			except:
				unassume = True

		if unassume:
			if request.session.has_key('assume_username'):
				del request.session['assume_username']
			if request.session.has_key('assume_referer'):
				request.assume_referer = request.session['assume_referer']
				del request.session['assume_referer']

	def process_view(self, request, view_func, view_args, view_kwargs):
		if request.GET.has_key('assume'):
			q = request.GET.copy()
			del q['assume']
			request.GET = q
			request.META['QUERY_STRING'] = q.urlencode()
			return redirect(request.build_absolute_uri())
		if request.GET.has_key('unassume'):
			if hasattr(request, 'assume_referer') and request.assume_referer:
				# Set in the process_request method
				return redirect(request.assume_referer)
			else:
				q = request.GET.copy()
				del q['unassume']
				request.GET = q
				request.META['QUERY_STRING'] = q.urlencode()
				return redirect(request.build_absolute_uri())
