class SessionsController < ApplicationController
	def new
		
	end
	def create
		user = User.find_by(email: params[:email])

		if user
			if user.authenticate(params[:password])
				session[:user_id] = user.id
				return redirect_to users_path
			end
				flash[:errors] = ["Incorrect Password"]
		else
			flash[:errors] = ["Incorrect Email"]
			p flash[:error]
		end
			return redirect_to new_session_path
	end
	def destroy
		session.clear
		return redirect_to new_session_path
	end
end
