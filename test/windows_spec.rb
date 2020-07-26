require_relative 'spec_helper'

set :backend, :winrm
set :os, :family => 'windows'

describe user('vagrant') do
  it { should exist }
  end
