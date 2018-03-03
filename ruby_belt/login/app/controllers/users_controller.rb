class UsersController < ApplicationController
	def index
		
	end
	def new
		
	end
	def create
		user = User.create(user_params)

		if user.valid?
			session[:user_id] = user.id
			return redirect_to users_path
		end
		flash[:errors] = user.errors.full_messages
		return redirect_to :back
	end
	def show
		
	end

	private
		def user_params
			params.require(:user).permit(:f_name, :l_name, :email, :password, :password_confirmation)
		end
end
