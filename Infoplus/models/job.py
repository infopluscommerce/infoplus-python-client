# coding: utf-8

"""
    Infoplus API

    Infoplus API.  # noqa: E501

    OpenAPI spec version: v3.0
    Contact: api@infopluscommerce.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from Infoplus.models.job_input import JobInput  # noqa: F401,E501
from Infoplus.models.job_output import JobOutput  # noqa: F401,E501
from Infoplus.models.job_step import JobStep  # noqa: F401,E501


class Job(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'create_date': 'datetime',
        'modify_date': 'datetime',
        'source_job_recipe_id': 'int',
        'assembly_quantity': 'int',
        'warehouse_id': 'int',
        'lob_id': 'int',
        'status': 'str',
        'order_no_id': 'float',
        'po_no_id': 'int',
        'work_batch_id': 'int',
        'layout': 'str',
        'track_assemblies': 'bool',
        'track_steps': 'bool',
        'job_no': 'str',
        'assembly_instructions': 'str',
        'inputs': 'list[JobInput]',
        'outputs': 'list[JobOutput]',
        'steps': 'list[JobStep]',
        'fulfillment_plan_id': 'int',
        'total_picks_putbacks': 'int',
        'completed_picks_putbacks': 'int',
        'total_assemblies': 'int',
        'completed_assemblies': 'int',
        'total_steps': 'int',
        'completed_steps': 'int',
        'total_receipts': 'int',
        'completed_receipts': 'int',
        'total_to_do': 'int',
        'completed_to_do': 'int',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'source_job_recipe_id': 'sourceJobRecipeId',
        'assembly_quantity': 'assemblyQuantity',
        'warehouse_id': 'warehouseId',
        'lob_id': 'lobId',
        'status': 'status',
        'order_no_id': 'orderNoId',
        'po_no_id': 'poNoId',
        'work_batch_id': 'workBatchId',
        'layout': 'layout',
        'track_assemblies': 'trackAssemblies',
        'track_steps': 'trackSteps',
        'job_no': 'jobNo',
        'assembly_instructions': 'assemblyInstructions',
        'inputs': 'inputs',
        'outputs': 'outputs',
        'steps': 'steps',
        'fulfillment_plan_id': 'fulfillmentPlanId',
        'total_picks_putbacks': 'totalPicksPutbacks',
        'completed_picks_putbacks': 'completedPicksPutbacks',
        'total_assemblies': 'totalAssemblies',
        'completed_assemblies': 'completedAssemblies',
        'total_steps': 'totalSteps',
        'completed_steps': 'completedSteps',
        'total_receipts': 'totalReceipts',
        'completed_receipts': 'completedReceipts',
        'total_to_do': 'totalToDo',
        'completed_to_do': 'completedToDo',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, create_date=None, modify_date=None, source_job_recipe_id=None, assembly_quantity=None, warehouse_id=None, lob_id=None, status=None, order_no_id=None, po_no_id=None, work_batch_id=None, layout=None, track_assemblies=False, track_steps=False, job_no=None, assembly_instructions=None, inputs=None, outputs=None, steps=None, fulfillment_plan_id=None, total_picks_putbacks=None, completed_picks_putbacks=None, total_assemblies=None, completed_assemblies=None, total_steps=None, completed_steps=None, total_receipts=None, completed_receipts=None, total_to_do=None, completed_to_do=None, custom_fields=None):  # noqa: E501
        """Job - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._create_date = None
        self._modify_date = None
        self._source_job_recipe_id = None
        self._assembly_quantity = None
        self._warehouse_id = None
        self._lob_id = None
        self._status = None
        self._order_no_id = None
        self._po_no_id = None
        self._work_batch_id = None
        self._layout = None
        self._track_assemblies = None
        self._track_steps = None
        self._job_no = None
        self._assembly_instructions = None
        self._inputs = None
        self._outputs = None
        self._steps = None
        self._fulfillment_plan_id = None
        self._total_picks_putbacks = None
        self._completed_picks_putbacks = None
        self._total_assemblies = None
        self._completed_assemblies = None
        self._total_steps = None
        self._completed_steps = None
        self._total_receipts = None
        self._completed_receipts = None
        self._total_to_do = None
        self._completed_to_do = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        if source_job_recipe_id is not None:
            self.source_job_recipe_id = source_job_recipe_id
        self.assembly_quantity = assembly_quantity
        self.warehouse_id = warehouse_id
        self.lob_id = lob_id
        if status is not None:
            self.status = status
        if order_no_id is not None:
            self.order_no_id = order_no_id
        if po_no_id is not None:
            self.po_no_id = po_no_id
        if work_batch_id is not None:
            self.work_batch_id = work_batch_id
        self.layout = layout
        self.track_assemblies = track_assemblies
        self.track_steps = track_steps
        if job_no is not None:
            self.job_no = job_no
        if assembly_instructions is not None:
            self.assembly_instructions = assembly_instructions
        if inputs is not None:
            self.inputs = inputs
        if outputs is not None:
            self.outputs = outputs
        if steps is not None:
            self.steps = steps
        self.fulfillment_plan_id = fulfillment_plan_id
        if total_picks_putbacks is not None:
            self.total_picks_putbacks = total_picks_putbacks
        if completed_picks_putbacks is not None:
            self.completed_picks_putbacks = completed_picks_putbacks
        if total_assemblies is not None:
            self.total_assemblies = total_assemblies
        if completed_assemblies is not None:
            self.completed_assemblies = completed_assemblies
        if total_steps is not None:
            self.total_steps = total_steps
        if completed_steps is not None:
            self.completed_steps = completed_steps
        if total_receipts is not None:
            self.total_receipts = total_receipts
        if completed_receipts is not None:
            self.completed_receipts = completed_receipts
        if total_to_do is not None:
            self.total_to_do = total_to_do
        if completed_to_do is not None:
            self.completed_to_do = completed_to_do
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this Job.  # noqa: E501


        :return: The id of this Job.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Job.


        :param id: The id of this Job.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def create_date(self):
        """Gets the create_date of this Job.  # noqa: E501


        :return: The create_date of this Job.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this Job.


        :param create_date: The create_date of this Job.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this Job.  # noqa: E501


        :return: The modify_date of this Job.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this Job.


        :param modify_date: The modify_date of this Job.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def source_job_recipe_id(self):
        """Gets the source_job_recipe_id of this Job.  # noqa: E501


        :return: The source_job_recipe_id of this Job.  # noqa: E501
        :rtype: int
        """
        return self._source_job_recipe_id

    @source_job_recipe_id.setter
    def source_job_recipe_id(self, source_job_recipe_id):
        """Sets the source_job_recipe_id of this Job.


        :param source_job_recipe_id: The source_job_recipe_id of this Job.  # noqa: E501
        :type: int
        """

        self._source_job_recipe_id = source_job_recipe_id

    @property
    def assembly_quantity(self):
        """Gets the assembly_quantity of this Job.  # noqa: E501


        :return: The assembly_quantity of this Job.  # noqa: E501
        :rtype: int
        """
        return self._assembly_quantity

    @assembly_quantity.setter
    def assembly_quantity(self, assembly_quantity):
        """Sets the assembly_quantity of this Job.


        :param assembly_quantity: The assembly_quantity of this Job.  # noqa: E501
        :type: int
        """
        if assembly_quantity is None:
            raise ValueError("Invalid value for `assembly_quantity`, must not be `None`")  # noqa: E501

        self._assembly_quantity = assembly_quantity

    @property
    def warehouse_id(self):
        """Gets the warehouse_id of this Job.  # noqa: E501


        :return: The warehouse_id of this Job.  # noqa: E501
        :rtype: int
        """
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, warehouse_id):
        """Sets the warehouse_id of this Job.


        :param warehouse_id: The warehouse_id of this Job.  # noqa: E501
        :type: int
        """
        if warehouse_id is None:
            raise ValueError("Invalid value for `warehouse_id`, must not be `None`")  # noqa: E501

        self._warehouse_id = warehouse_id

    @property
    def lob_id(self):
        """Gets the lob_id of this Job.  # noqa: E501


        :return: The lob_id of this Job.  # noqa: E501
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """Sets the lob_id of this Job.


        :param lob_id: The lob_id of this Job.  # noqa: E501
        :type: int
        """
        if lob_id is None:
            raise ValueError("Invalid value for `lob_id`, must not be `None`")  # noqa: E501

        self._lob_id = lob_id

    @property
    def status(self):
        """Gets the status of this Job.  # noqa: E501


        :return: The status of this Job.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Job.


        :param status: The status of this Job.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def order_no_id(self):
        """Gets the order_no_id of this Job.  # noqa: E501


        :return: The order_no_id of this Job.  # noqa: E501
        :rtype: float
        """
        return self._order_no_id

    @order_no_id.setter
    def order_no_id(self, order_no_id):
        """Sets the order_no_id of this Job.


        :param order_no_id: The order_no_id of this Job.  # noqa: E501
        :type: float
        """

        self._order_no_id = order_no_id

    @property
    def po_no_id(self):
        """Gets the po_no_id of this Job.  # noqa: E501


        :return: The po_no_id of this Job.  # noqa: E501
        :rtype: int
        """
        return self._po_no_id

    @po_no_id.setter
    def po_no_id(self, po_no_id):
        """Sets the po_no_id of this Job.


        :param po_no_id: The po_no_id of this Job.  # noqa: E501
        :type: int
        """

        self._po_no_id = po_no_id

    @property
    def work_batch_id(self):
        """Gets the work_batch_id of this Job.  # noqa: E501


        :return: The work_batch_id of this Job.  # noqa: E501
        :rtype: int
        """
        return self._work_batch_id

    @work_batch_id.setter
    def work_batch_id(self, work_batch_id):
        """Sets the work_batch_id of this Job.


        :param work_batch_id: The work_batch_id of this Job.  # noqa: E501
        :type: int
        """

        self._work_batch_id = work_batch_id

    @property
    def layout(self):
        """Gets the layout of this Job.  # noqa: E501


        :return: The layout of this Job.  # noqa: E501
        :rtype: str
        """
        return self._layout

    @layout.setter
    def layout(self, layout):
        """Sets the layout of this Job.


        :param layout: The layout of this Job.  # noqa: E501
        :type: str
        """
        if layout is None:
            raise ValueError("Invalid value for `layout`, must not be `None`")  # noqa: E501

        self._layout = layout

    @property
    def track_assemblies(self):
        """Gets the track_assemblies of this Job.  # noqa: E501


        :return: The track_assemblies of this Job.  # noqa: E501
        :rtype: bool
        """
        return self._track_assemblies

    @track_assemblies.setter
    def track_assemblies(self, track_assemblies):
        """Sets the track_assemblies of this Job.


        :param track_assemblies: The track_assemblies of this Job.  # noqa: E501
        :type: bool
        """
        if track_assemblies is None:
            raise ValueError("Invalid value for `track_assemblies`, must not be `None`")  # noqa: E501

        self._track_assemblies = track_assemblies

    @property
    def track_steps(self):
        """Gets the track_steps of this Job.  # noqa: E501


        :return: The track_steps of this Job.  # noqa: E501
        :rtype: bool
        """
        return self._track_steps

    @track_steps.setter
    def track_steps(self, track_steps):
        """Sets the track_steps of this Job.


        :param track_steps: The track_steps of this Job.  # noqa: E501
        :type: bool
        """
        if track_steps is None:
            raise ValueError("Invalid value for `track_steps`, must not be `None`")  # noqa: E501

        self._track_steps = track_steps

    @property
    def job_no(self):
        """Gets the job_no of this Job.  # noqa: E501


        :return: The job_no of this Job.  # noqa: E501
        :rtype: str
        """
        return self._job_no

    @job_no.setter
    def job_no(self, job_no):
        """Sets the job_no of this Job.


        :param job_no: The job_no of this Job.  # noqa: E501
        :type: str
        """

        self._job_no = job_no

    @property
    def assembly_instructions(self):
        """Gets the assembly_instructions of this Job.  # noqa: E501


        :return: The assembly_instructions of this Job.  # noqa: E501
        :rtype: str
        """
        return self._assembly_instructions

    @assembly_instructions.setter
    def assembly_instructions(self, assembly_instructions):
        """Sets the assembly_instructions of this Job.


        :param assembly_instructions: The assembly_instructions of this Job.  # noqa: E501
        :type: str
        """

        self._assembly_instructions = assembly_instructions

    @property
    def inputs(self):
        """Gets the inputs of this Job.  # noqa: E501


        :return: The inputs of this Job.  # noqa: E501
        :rtype: list[JobInput]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this Job.


        :param inputs: The inputs of this Job.  # noqa: E501
        :type: list[JobInput]
        """

        self._inputs = inputs

    @property
    def outputs(self):
        """Gets the outputs of this Job.  # noqa: E501


        :return: The outputs of this Job.  # noqa: E501
        :rtype: list[JobOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this Job.


        :param outputs: The outputs of this Job.  # noqa: E501
        :type: list[JobOutput]
        """

        self._outputs = outputs

    @property
    def steps(self):
        """Gets the steps of this Job.  # noqa: E501


        :return: The steps of this Job.  # noqa: E501
        :rtype: list[JobStep]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this Job.


        :param steps: The steps of this Job.  # noqa: E501
        :type: list[JobStep]
        """

        self._steps = steps

    @property
    def fulfillment_plan_id(self):
        """Gets the fulfillment_plan_id of this Job.  # noqa: E501


        :return: The fulfillment_plan_id of this Job.  # noqa: E501
        :rtype: int
        """
        return self._fulfillment_plan_id

    @fulfillment_plan_id.setter
    def fulfillment_plan_id(self, fulfillment_plan_id):
        """Sets the fulfillment_plan_id of this Job.


        :param fulfillment_plan_id: The fulfillment_plan_id of this Job.  # noqa: E501
        :type: int
        """
        if fulfillment_plan_id is None:
            raise ValueError("Invalid value for `fulfillment_plan_id`, must not be `None`")  # noqa: E501

        self._fulfillment_plan_id = fulfillment_plan_id

    @property
    def total_picks_putbacks(self):
        """Gets the total_picks_putbacks of this Job.  # noqa: E501


        :return: The total_picks_putbacks of this Job.  # noqa: E501
        :rtype: int
        """
        return self._total_picks_putbacks

    @total_picks_putbacks.setter
    def total_picks_putbacks(self, total_picks_putbacks):
        """Sets the total_picks_putbacks of this Job.


        :param total_picks_putbacks: The total_picks_putbacks of this Job.  # noqa: E501
        :type: int
        """

        self._total_picks_putbacks = total_picks_putbacks

    @property
    def completed_picks_putbacks(self):
        """Gets the completed_picks_putbacks of this Job.  # noqa: E501


        :return: The completed_picks_putbacks of this Job.  # noqa: E501
        :rtype: int
        """
        return self._completed_picks_putbacks

    @completed_picks_putbacks.setter
    def completed_picks_putbacks(self, completed_picks_putbacks):
        """Sets the completed_picks_putbacks of this Job.


        :param completed_picks_putbacks: The completed_picks_putbacks of this Job.  # noqa: E501
        :type: int
        """

        self._completed_picks_putbacks = completed_picks_putbacks

    @property
    def total_assemblies(self):
        """Gets the total_assemblies of this Job.  # noqa: E501


        :return: The total_assemblies of this Job.  # noqa: E501
        :rtype: int
        """
        return self._total_assemblies

    @total_assemblies.setter
    def total_assemblies(self, total_assemblies):
        """Sets the total_assemblies of this Job.


        :param total_assemblies: The total_assemblies of this Job.  # noqa: E501
        :type: int
        """

        self._total_assemblies = total_assemblies

    @property
    def completed_assemblies(self):
        """Gets the completed_assemblies of this Job.  # noqa: E501


        :return: The completed_assemblies of this Job.  # noqa: E501
        :rtype: int
        """
        return self._completed_assemblies

    @completed_assemblies.setter
    def completed_assemblies(self, completed_assemblies):
        """Sets the completed_assemblies of this Job.


        :param completed_assemblies: The completed_assemblies of this Job.  # noqa: E501
        :type: int
        """

        self._completed_assemblies = completed_assemblies

    @property
    def total_steps(self):
        """Gets the total_steps of this Job.  # noqa: E501


        :return: The total_steps of this Job.  # noqa: E501
        :rtype: int
        """
        return self._total_steps

    @total_steps.setter
    def total_steps(self, total_steps):
        """Sets the total_steps of this Job.


        :param total_steps: The total_steps of this Job.  # noqa: E501
        :type: int
        """

        self._total_steps = total_steps

    @property
    def completed_steps(self):
        """Gets the completed_steps of this Job.  # noqa: E501


        :return: The completed_steps of this Job.  # noqa: E501
        :rtype: int
        """
        return self._completed_steps

    @completed_steps.setter
    def completed_steps(self, completed_steps):
        """Sets the completed_steps of this Job.


        :param completed_steps: The completed_steps of this Job.  # noqa: E501
        :type: int
        """

        self._completed_steps = completed_steps

    @property
    def total_receipts(self):
        """Gets the total_receipts of this Job.  # noqa: E501


        :return: The total_receipts of this Job.  # noqa: E501
        :rtype: int
        """
        return self._total_receipts

    @total_receipts.setter
    def total_receipts(self, total_receipts):
        """Sets the total_receipts of this Job.


        :param total_receipts: The total_receipts of this Job.  # noqa: E501
        :type: int
        """

        self._total_receipts = total_receipts

    @property
    def completed_receipts(self):
        """Gets the completed_receipts of this Job.  # noqa: E501


        :return: The completed_receipts of this Job.  # noqa: E501
        :rtype: int
        """
        return self._completed_receipts

    @completed_receipts.setter
    def completed_receipts(self, completed_receipts):
        """Sets the completed_receipts of this Job.


        :param completed_receipts: The completed_receipts of this Job.  # noqa: E501
        :type: int
        """

        self._completed_receipts = completed_receipts

    @property
    def total_to_do(self):
        """Gets the total_to_do of this Job.  # noqa: E501


        :return: The total_to_do of this Job.  # noqa: E501
        :rtype: int
        """
        return self._total_to_do

    @total_to_do.setter
    def total_to_do(self, total_to_do):
        """Sets the total_to_do of this Job.


        :param total_to_do: The total_to_do of this Job.  # noqa: E501
        :type: int
        """

        self._total_to_do = total_to_do

    @property
    def completed_to_do(self):
        """Gets the completed_to_do of this Job.  # noqa: E501


        :return: The completed_to_do of this Job.  # noqa: E501
        :rtype: int
        """
        return self._completed_to_do

    @completed_to_do.setter
    def completed_to_do(self, completed_to_do):
        """Sets the completed_to_do of this Job.


        :param completed_to_do: The completed_to_do of this Job.  # noqa: E501
        :type: int
        """

        self._completed_to_do = completed_to_do

    @property
    def custom_fields(self):
        """Gets the custom_fields of this Job.  # noqa: E501


        :return: The custom_fields of this Job.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this Job.


        :param custom_fields: The custom_fields of this Job.  # noqa: E501
        :type: dict(str, object)
        """

        self._custom_fields = custom_fields

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Job):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
