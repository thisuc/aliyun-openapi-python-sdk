# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkdrds.endpoint import endpoint_data

class PrecheckMyCatEvaluateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Drds', '2019-01-23', 'PrecheckMyCatEvaluate','Drds')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SequenceType(self):
		return self.get_query_params().get('SequenceType')

	def set_SequenceType(self,SequenceType):
		self.add_query_param('SequenceType',SequenceType)

	def get_TaskName(self):
		return self.get_query_params().get('TaskName')

	def set_TaskName(self,TaskName):
		self.add_query_param('TaskName',TaskName)

	def get_SchemaUrl(self):
		return self.get_query_params().get('SchemaUrl')

	def set_SchemaUrl(self,SchemaUrl):
		self.add_query_param('SchemaUrl',SchemaUrl)

	def get_BusPeakQps(self):
		return self.get_query_params().get('BusPeakQps')

	def set_BusPeakQps(self,BusPeakQps):
		self.add_query_param('BusPeakQps',BusPeakQps)

	def get_QpsIncPercent(self):
		return self.get_query_params().get('QpsIncPercent')

	def set_QpsIncPercent(self,QpsIncPercent):
		self.add_query_param('QpsIncPercent',QpsIncPercent)

	def get_ServerUrl(self):
		return self.get_query_params().get('ServerUrl')

	def set_ServerUrl(self,ServerUrl):
		self.add_query_param('ServerUrl',ServerUrl)

	def get_CapacityIncPercent(self):
		return self.get_query_params().get('CapacityIncPercent')

	def set_CapacityIncPercent(self,CapacityIncPercent):
		self.add_query_param('CapacityIncPercent',CapacityIncPercent)

	def get_RuleUrl(self):
		return self.get_query_params().get('RuleUrl')

	def set_RuleUrl(self,RuleUrl):
		self.add_query_param('RuleUrl',RuleUrl)

	def get_ImportDbLists(self):
		return self.get_query_params().get('ImportDbLists')

	def set_ImportDbLists(self, ImportDbLists):
		for depth1 in range(len(ImportDbLists)):
			if ImportDbLists[depth1] is not None:
				self.add_query_param('ImportDbList.' + str(depth1 + 1) , ImportDbLists[depth1])