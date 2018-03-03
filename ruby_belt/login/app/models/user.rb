class User < ActiveRecord::Base
  has_secure_password

  validates :f_name, :l_name, :password, presence: true
  validates :email, presence: true, uniqueness: true
end
