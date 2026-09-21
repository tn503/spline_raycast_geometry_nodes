import bpy
import mathutils
import os
import typing


# Import node groups from Blender essentials library
datafiles_path = bpy.utils.system_resource('DATAFILES')
lib_relpath = "assets/nodes/geometry_nodes_essentials.blend"
lib_path = os.path.join(datafiles_path, lib_relpath)
with bpy.data.libraries.load(lib_path, link=True)  as (data_src, data_dst):
	data_dst.node_groups = []
	if "Is Edge Loose" in data_src.node_groups:
		data_dst.node_groups.append("Is Edge Loose")


def spline_raycast_nodes_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize spline_raycast_nodes node group"""
    spline_raycast_nodes_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="spline_raycast_nodes")

    spline_raycast_nodes_1.color_tag = 'NONE'
    spline_raycast_nodes_1.description = ""
    spline_raycast_nodes_1.default_group_node_width = 140
    spline_raycast_nodes_1.is_modifier = True
    spline_raycast_nodes_1.show_modifier_manage_panel = True

    # spline_raycast_nodes_1 interface

    # Socket Geometry
    geometry_socket = spline_raycast_nodes_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = spline_raycast_nodes_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Socket Target Object
    target_object_socket = spline_raycast_nodes_1.interface.new_socket(name="Target Object", in_out='INPUT', socket_type='NodeSocketObject')
    target_object_socket.attribute_domain = 'POINT'
    target_object_socket.default_input = 'VALUE'
    target_object_socket.structure_type = 'AUTO'

    # Initialize spline_raycast_nodes_1 nodes

    # Node Group Input
    group_input = spline_raycast_nodes_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Group Output
    group_output = spline_raycast_nodes_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Offset Point in Curve
    offset_point_in_curve = spline_raycast_nodes_1.nodes.new("GeometryNodeOffsetPointInCurve")
    offset_point_in_curve.name = "Offset Point in Curve"
    offset_point_in_curve.show_options = True
    # Point Index
    offset_point_in_curve.inputs[0].default_value = 0
    # Offset
    offset_point_in_curve.inputs[1].default_value = 1

    # Node Sample Index
    sample_index = spline_raycast_nodes_1.nodes.new("GeometryNodeSampleIndex")
    sample_index.name = "Sample Index"
    sample_index.show_options = True
    sample_index.clamp = False
    sample_index.data_type = 'FLOAT_VECTOR'
    sample_index.domain = 'POINT'

    # Node Position
    position = spline_raycast_nodes_1.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"
    position.show_options = True

    # Node Raycast
    raycast = spline_raycast_nodes_1.nodes.new("GeometryNodeRaycast")
    raycast.name = "Raycast"
    raycast.show_options = True
    raycast.data_type = 'INT'
    # Interpolation
    raycast.inputs[2].default_value = 'Interpolated'

    # Node Object Info
    object_info = spline_raycast_nodes_1.nodes.new("GeometryNodeObjectInfo")
    object_info.name = "Object Info"
    object_info.show_options = True
    object_info.transform_space = 'ORIGINAL'
    # As Instance
    object_info.inputs[1].default_value = False

    # Node Store Named Attribute.001
    store_named_attribute_001 = spline_raycast_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_001.name = "Store Named Attribute.001"
    store_named_attribute_001.show_options = True
    store_named_attribute_001.data_type = 'FLOAT'
    store_named_attribute_001.domain = 'POINT'
    # Name
    store_named_attribute_001.inputs[2].default_value = "hit"

    # Node Vector Math
    vector_math = spline_raycast_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.show_options = True
    vector_math.operation = 'SUBTRACT'

    # Node Vector Math.001
    vector_math_001 = spline_raycast_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.show_options = True
    vector_math_001.operation = 'LENGTH'

    # Node Boolean Math
    boolean_math = spline_raycast_nodes_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math.name = "Boolean Math"
    boolean_math.show_options = True
    boolean_math.operation = 'AND'

    # Node Store Named Attribute.003
    store_named_attribute_003 = spline_raycast_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_003.name = "Store Named Attribute.003"
    store_named_attribute_003.show_options = True
    store_named_attribute_003.data_type = 'FLOAT'
    store_named_attribute_003.domain = 'CURVE'
    # Selection
    store_named_attribute_003.inputs[1].default_value = True
    # Name
    store_named_attribute_003.inputs[2].default_value = "hit2"

    # Node Accumulate Field
    accumulate_field = spline_raycast_nodes_1.nodes.new("GeometryNodeAccumulateField")
    accumulate_field.name = "Accumulate Field"
    accumulate_field.show_options = True
    accumulate_field.data_type = 'FLOAT'
    accumulate_field.domain = 'POINT'

    # Node Curve of Point.001
    curve_of_point_001 = spline_raycast_nodes_1.nodes.new("GeometryNodeCurveOfPoint")
    curve_of_point_001.name = "Curve of Point.001"
    curve_of_point_001.show_options = True
    # Point Index
    curve_of_point_001.inputs[0].default_value = 0

    # Node Named Attribute.001
    named_attribute_001 = spline_raycast_nodes_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_001.name = "Named Attribute.001"
    named_attribute_001.show_options = True
    named_attribute_001.data_type = 'FLOAT'
    # Name
    named_attribute_001.inputs[0].default_value = "hit"

    # Node Join Geometry
    join_geometry = spline_raycast_nodes_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"
    join_geometry.show_options = True

    # Node Spline Length
    spline_length = spline_raycast_nodes_1.nodes.new("GeometryNodeSplineLength")
    spline_length.name = "Spline Length"
    spline_length.show_options = True

    # Node Math
    math = spline_raycast_nodes_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.show_options = True
    math.operation = 'DIVIDE'
    math.use_clamp = False

    # Node Math.001
    math_001 = spline_raycast_nodes_1.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.show_options = True
    math_001.operation = 'ADD'
    math_001.use_clamp = False

    # Node Spline Parameter
    spline_parameter = spline_raycast_nodes_1.nodes.new("GeometryNodeSplineParameter")
    spline_parameter.name = "Spline Parameter"
    spline_parameter.show_options = True

    # Node Store Named Attribute.002
    store_named_attribute_002 = spline_raycast_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_002.name = "Store Named Attribute.002"
    store_named_attribute_002.show_options = True
    store_named_attribute_002.data_type = 'INT'
    store_named_attribute_002.domain = 'POINT'
    # Name
    store_named_attribute_002.inputs[2].default_value = "hit_island"

    # Node Mesh Island.001
    mesh_island_001 = spline_raycast_nodes_1.nodes.new("GeometryNodeInputMeshIsland")
    mesh_island_001.name = "Mesh Island.001"
    mesh_island_001.show_options = True

    # Node Integer Math
    integer_math = spline_raycast_nodes_1.nodes.new("FunctionNodeIntegerMath")
    integer_math.name = "Integer Math"
    integer_math.show_options = True
    integer_math.operation = 'ADD'
    # Value_001
    integer_math.inputs[1].default_value = 1

    # Node Store Named Attribute.004
    store_named_attribute_004 = spline_raycast_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_004.name = "Store Named Attribute.004"
    store_named_attribute_004.show_options = True
    store_named_attribute_004.data_type = 'INT'
    store_named_attribute_004.domain = 'CURVE'
    # Selection
    store_named_attribute_004.inputs[1].default_value = True
    # Name
    store_named_attribute_004.inputs[2].default_value = "hit_island2"

    # Node Accumulate Field.002
    accumulate_field_002 = spline_raycast_nodes_1.nodes.new("GeometryNodeAccumulateField")
    accumulate_field_002.name = "Accumulate Field.002"
    accumulate_field_002.show_options = True
    accumulate_field_002.data_type = 'INT'
    accumulate_field_002.domain = 'POINT'

    # Node Named Attribute
    named_attribute = spline_raycast_nodes_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.name = "Named Attribute"
    named_attribute.show_options = True
    named_attribute.data_type = 'INT'
    # Name
    named_attribute.inputs[0].default_value = "hit_island"

    # Node Split to Instances.001
    split_to_instances_001 = spline_raycast_nodes_1.nodes.new("GeometryNodeSplitToInstances")
    split_to_instances_001.name = "Split to Instances.001"
    split_to_instances_001.show_options = True
    split_to_instances_001.domain = 'CURVE'

    # Node Compare.003
    compare_003 = spline_raycast_nodes_1.nodes.new("FunctionNodeCompare")
    compare_003.name = "Compare.003"
    compare_003.show_options = True
    compare_003.data_type = 'INT'
    compare_003.mode = 'ELEMENT'
    compare_003.operation = 'GREATER_THAN'
    # B
    compare_003.inputs[1].default_value = 0

    # Node Named Attribute.004
    named_attribute_004 = spline_raycast_nodes_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_004.name = "Named Attribute.004"
    named_attribute_004.show_options = True
    named_attribute_004.data_type = 'INT'
    # Name
    named_attribute_004.inputs[0].default_value = "hit_island2"

    # Node For Each Geometry Element Input
    for_each_geometry_element_input = spline_raycast_nodes_1.nodes.new("GeometryNodeForeachGeometryElementInput")
    for_each_geometry_element_input.name = "For Each Geometry Element Input"
    for_each_geometry_element_input.show_options = True
    # Node For Each Geometry Element Output
    for_each_geometry_element_output = spline_raycast_nodes_1.nodes.new("GeometryNodeForeachGeometryElementOutput")
    for_each_geometry_element_output.name = "For Each Geometry Element Output"
    for_each_geometry_element_output.show_options = True
    for_each_geometry_element_output.active_generation_index = 1
    for_each_geometry_element_output.active_input_index = 0
    for_each_geometry_element_output.active_main_index = 0
    for_each_geometry_element_output.domain = 'INSTANCE'
    for_each_geometry_element_output.generation_items.clear()
    for_each_geometry_element_output.generation_items.new('GEOMETRY', "Geometry")
    for_each_geometry_element_output.generation_items[0].domain = 'POINT'
    for_each_geometry_element_output.generation_items.new('GEOMETRY', "Curve")
    for_each_geometry_element_output.generation_items[1].domain = 'POINT'
    for_each_geometry_element_output.input_items.clear()
    for_each_geometry_element_output.input_items.new('INT', "Group ID")
    for_each_geometry_element_output.inspection_index = 0
    for_each_geometry_element_output.main_items.clear()
    for_each_geometry_element_output.panel_states[0].is_collapsed = False

    # Node Realize Instances
    realize_instances = spline_raycast_nodes_1.nodes.new("GeometryNodeRealizeInstances")
    realize_instances.name = "Realize Instances"
    realize_instances.show_options = True
    realize_instances.realize_to_point_domain = False
    # Selection
    realize_instances.inputs[1].default_value = True
    # Realize All
    realize_instances.inputs[2].default_value = True
    # Depth
    realize_instances.inputs[3].default_value = 0

    # Node Set Position.003
    set_position_003 = spline_raycast_nodes_1.nodes.new("GeometryNodeSetPosition")
    set_position_003.name = "Set Position.003"
    set_position_003.show_options = True
    # Position
    set_position_003.inputs[2].default_value = (0.0, 0.0, 0.0)

    # Node Boolean Math.002
    boolean_math_002 = spline_raycast_nodes_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_002.name = "Boolean Math.002"
    boolean_math_002.show_options = True
    boolean_math_002.operation = 'AND'

    # Node Compare.004
    compare_004 = spline_raycast_nodes_1.nodes.new("FunctionNodeCompare")
    compare_004.name = "Compare.004"
    compare_004.show_options = True
    compare_004.data_type = 'FLOAT'
    compare_004.mode = 'ELEMENT'
    compare_004.operation = 'GREATER_THAN'
    # B
    compare_004.inputs[1].default_value = 0.0

    # Node Named Attribute.005
    named_attribute_005 = spline_raycast_nodes_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_005.name = "Named Attribute.005"
    named_attribute_005.show_options = True
    named_attribute_005.data_type = 'FLOAT'
    # Name
    named_attribute_005.inputs[0].default_value = "hit2"

    # Node Compare.005
    compare_005 = spline_raycast_nodes_1.nodes.new("FunctionNodeCompare")
    compare_005.name = "Compare.005"
    compare_005.show_options = True
    compare_005.data_type = 'FLOAT'
    compare_005.mode = 'ELEMENT'
    compare_005.operation = 'GREATER_THAN'

    # Node Spline Parameter.002
    spline_parameter_002 = spline_raycast_nodes_1.nodes.new("GeometryNodeSplineParameter")
    spline_parameter_002.name = "Spline Parameter.002"
    spline_parameter_002.show_options = True

    # Node Accumulate Field.003
    accumulate_field_003 = spline_raycast_nodes_1.nodes.new("GeometryNodeAccumulateField")
    accumulate_field_003.name = "Accumulate Field.003"
    accumulate_field_003.show_options = True
    accumulate_field_003.data_type = 'FLOAT_VECTOR'
    accumulate_field_003.domain = 'POINT'

    # Node Curve of Point.002
    curve_of_point_002 = spline_raycast_nodes_1.nodes.new("GeometryNodeCurveOfPoint")
    curve_of_point_002.name = "Curve of Point.002"
    curve_of_point_002.show_options = True
    # Point Index
    curve_of_point_002.inputs[0].default_value = 0

    # Node Position.002
    position_002 = spline_raycast_nodes_1.nodes.new("GeometryNodeInputPosition")
    position_002.name = "Position.002"
    position_002.show_options = True

    # Node Vector Math.005
    vector_math_005 = spline_raycast_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math_005.name = "Vector Math.005"
    vector_math_005.show_options = True
    vector_math_005.operation = 'SCALE'

    # Node Domain Size.002
    domain_size_002 = spline_raycast_nodes_1.nodes.new("GeometryNodeAttributeDomainSize")
    domain_size_002.name = "Domain Size.002"
    domain_size_002.show_options = True
    domain_size_002.component = 'CURVE'

    # Node Math.003
    math_003 = spline_raycast_nodes_1.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.show_options = True
    math_003.operation = 'DIVIDE'
    math_003.use_clamp = False
    # Value
    math_003.inputs[0].default_value = 1.0

    # Node Vector Math.006
    vector_math_006 = spline_raycast_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math_006.name = "Vector Math.006"
    vector_math_006.show_options = True
    vector_math_006.operation = 'SUBTRACT'

    # Node Vector Math.007
    vector_math_007 = spline_raycast_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math_007.name = "Vector Math.007"
    vector_math_007.show_options = True
    vector_math_007.operation = 'SCALE'

    # Node Map Range.001
    map_range_001 = spline_raycast_nodes_1.nodes.new("ShaderNodeMapRange")
    map_range_001.name = "Map Range.001"
    map_range_001.show_options = True
    map_range_001.clamp = True
    map_range_001.data_type = 'FLOAT'
    map_range_001.interpolation_type = 'LINEAR'
    # From Max
    map_range_001.inputs[2].default_value = 1.0
    # To Min
    map_range_001.inputs[3].default_value = 0.0
    # To Max
    map_range_001.inputs[4].default_value = 1.0

    # Node Separate Geometry.001
    separate_geometry_001 = spline_raycast_nodes_1.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry_001.name = "Separate Geometry.001"
    separate_geometry_001.show_options = True
    separate_geometry_001.domain = 'CURVE'

    # Node Compare.006
    compare_006 = spline_raycast_nodes_1.nodes.new("FunctionNodeCompare")
    compare_006.name = "Compare.006"
    compare_006.show_options = True
    compare_006.data_type = 'FLOAT'
    compare_006.mode = 'ELEMENT'
    compare_006.operation = 'GREATER_THAN'
    # B
    compare_006.inputs[1].default_value = 0.0

    # Node Named Attribute.006
    named_attribute_006 = spline_raycast_nodes_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_006.name = "Named Attribute.006"
    named_attribute_006.show_options = True
    named_attribute_006.data_type = 'FLOAT'
    # Name
    named_attribute_006.inputs[0].default_value = "hit2"

    # Node Group Input.001
    group_input_001 = spline_raycast_nodes_1.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.show_options = True

    # Node Object Info.001
    object_info_001 = spline_raycast_nodes_1.nodes.new("GeometryNodeObjectInfo")
    object_info_001.name = "Object Info.001"
    object_info_001.show_options = True
    object_info_001.transform_space = 'ORIGINAL'
    # As Instance
    object_info_001.inputs[1].default_value = False

    # Node Compare
    compare = spline_raycast_nodes_1.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.show_options = True
    compare.data_type = 'INT'
    compare.mode = 'ELEMENT'
    compare.operation = 'EQUAL'

    # Node Mesh Island
    mesh_island = spline_raycast_nodes_1.nodes.new("GeometryNodeInputMeshIsland")
    mesh_island.name = "Mesh Island"
    mesh_island.show_options = True

    # Node Mesh to Curve
    mesh_to_curve = spline_raycast_nodes_1.nodes.new("GeometryNodeMeshToCurve")
    mesh_to_curve.name = "Mesh to Curve"
    mesh_to_curve.show_options = True
    mesh_to_curve.mode = 'EDGES'

    # Node Is Edge Loose
    is_edge_loose = spline_raycast_nodes_1.nodes.new("GeometryNodeGroup")
    is_edge_loose.name = "Is Edge Loose"
    # Finding linked library node group
    for node_group in bpy.data.node_groups:
        if (
            node_group.name == "Is Edge Loose"
            and node_group.bl_idname == 'GeometryNodeTree'
        ):
            is_edge_loose.node_tree = node_group
    if is_edge_loose.node_tree is None:
        print("Couldn't find node group Is Edge Loose, failing")
        return

    # Node Boolean Math.001
    boolean_math_001 = spline_raycast_nodes_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_001.name = "Boolean Math.001"
    boolean_math_001.show_options = True
    boolean_math_001.operation = 'AND'

    # Node Join Geometry.001
    join_geometry_001 = spline_raycast_nodes_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_001.name = "Join Geometry.001"
    join_geometry_001.show_options = True

    # Node Integer Math.001
    integer_math_001 = spline_raycast_nodes_1.nodes.new("FunctionNodeIntegerMath")
    integer_math_001.name = "Integer Math.001"
    integer_math_001.show_options = True
    integer_math_001.operation = 'ADD'
    # Value_001
    integer_math_001.inputs[1].default_value = 1

    # Node Store Named Attribute
    store_named_attribute = spline_raycast_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.show_options = True
    store_named_attribute.data_type = 'BOOLEAN'
    store_named_attribute.domain = 'POINT'
    # Name
    store_named_attribute.inputs[2].default_value = "endpoint"
    # Value
    store_named_attribute.inputs[3].default_value = True

    # Node Vertex Neighbors
    vertex_neighbors = spline_raycast_nodes_1.nodes.new("GeometryNodeInputMeshVertexNeighbors")
    vertex_neighbors.name = "Vertex Neighbors"
    vertex_neighbors.show_options = True

    # Node Compare.001
    compare_001 = spline_raycast_nodes_1.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.show_options = True
    compare_001.data_type = 'INT'
    compare_001.mode = 'ELEMENT'
    compare_001.operation = 'EQUAL'
    # B
    compare_001.inputs[1].default_value = 1

    # Node Reverse Curve
    reverse_curve = spline_raycast_nodes_1.nodes.new("GeometryNodeReverseCurve")
    reverse_curve.name = "Reverse Curve"
    reverse_curve.show_options = True

    # Node Points of Curve
    points_of_curve = spline_raycast_nodes_1.nodes.new("GeometryNodePointsOfCurve")
    points_of_curve.name = "Points of Curve"
    points_of_curve.show_options = True
    # Curve Index
    points_of_curve.inputs[0].default_value = 0
    # Weights
    points_of_curve.inputs[1].default_value = 0.0
    # Sort Index
    points_of_curve.inputs[2].default_value = -1

    # Node Sample Index.001
    sample_index_001 = spline_raycast_nodes_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_001.name = "Sample Index.001"
    sample_index_001.show_options = True
    sample_index_001.clamp = False
    sample_index_001.data_type = 'BOOLEAN'
    sample_index_001.domain = 'POINT'

    # Node Named Attribute.002
    named_attribute_002 = spline_raycast_nodes_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_002.name = "Named Attribute.002"
    named_attribute_002.show_options = True
    named_attribute_002.data_type = 'BOOLEAN'
    # Name
    named_attribute_002.inputs[0].default_value = "endpoint"

    # Node Boolean Math.003
    boolean_math_003 = spline_raycast_nodes_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_003.name = "Boolean Math.003"
    boolean_math_003.show_options = True
    boolean_math_003.operation = 'NOT'

    # Node Points
    points = spline_raycast_nodes_1.nodes.new("GeometryNodePoints")
    points.name = "Points"
    points.show_options = True

    # Node Sample Index.002
    sample_index_002 = spline_raycast_nodes_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_002.name = "Sample Index.002"
    sample_index_002.show_options = True
    sample_index_002.clamp = False
    sample_index_002.data_type = 'FLOAT'
    sample_index_002.domain = 'CURVE'

    # Node Index
    index = spline_raycast_nodes_1.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"
    index.show_options = True

    # Node Sample Curve
    sample_curve = spline_raycast_nodes_1.nodes.new("GeometryNodeSampleCurve")
    sample_curve.name = "Sample Curve"
    sample_curve.show_options = True
    sample_curve.data_type = 'INT'
    sample_curve.mode = 'FACTOR'
    sample_curve.use_all_curves = False

    # Node Named Attribute.003
    named_attribute_003 = spline_raycast_nodes_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_003.name = "Named Attribute.003"
    named_attribute_003.show_options = True
    named_attribute_003.data_type = 'FLOAT'
    # Name
    named_attribute_003.inputs[0].default_value = "hit2"

    # Node Index.001
    index_001 = spline_raycast_nodes_1.nodes.new("GeometryNodeInputIndex")
    index_001.name = "Index.001"
    index_001.show_options = True

    # Node Trim Curve.001
    trim_curve_001 = spline_raycast_nodes_1.nodes.new("GeometryNodeTrimCurve")
    trim_curve_001.name = "Trim Curve.001"
    trim_curve_001.show_options = True
    trim_curve_001.mode = 'FACTOR'
    # Selection
    trim_curve_001.inputs[1].default_value = True
    # Start
    trim_curve_001.inputs[2].default_value = 0.0

    # Node Interpolate Curves
    interpolate_curves = spline_raycast_nodes_1.nodes.new("GeometryNodeInterpolateCurves")
    interpolate_curves.name = "Interpolate Curves"
    interpolate_curves.show_options = True
    # Guide Up
    interpolate_curves.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Guide Group ID
    interpolate_curves.inputs[2].default_value = 0
    # Point Up
    interpolate_curves.inputs[4].default_value = (0.0, 0.0, 0.0)
    # Point Group ID
    interpolate_curves.inputs[5].default_value = 0
    # Max Neighbors
    interpolate_curves.inputs[6].default_value = 1

    # Node Points to Curves
    points_to_curves = spline_raycast_nodes_1.nodes.new("GeometryNodePointsToCurves")
    points_to_curves.name = "Points to Curves"
    points_to_curves.show_options = True
    # Weight
    points_to_curves.inputs[2].default_value = 0.0

    # Node Delete Geometry
    delete_geometry = spline_raycast_nodes_1.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.name = "Delete Geometry"
    delete_geometry.show_options = True
    delete_geometry.domain = 'POINT'
    delete_geometry.mode = 'ALL'

    # Node Curve of Point
    curve_of_point = spline_raycast_nodes_1.nodes.new("GeometryNodeCurveOfPoint")
    curve_of_point.name = "Curve of Point"
    curve_of_point.show_options = True
    # Point Index
    curve_of_point.inputs[0].default_value = 0

    # Node Compare.002
    compare_002 = spline_raycast_nodes_1.nodes.new("FunctionNodeCompare")
    compare_002.name = "Compare.002"
    compare_002.show_options = True
    compare_002.data_type = 'INT'
    compare_002.mode = 'ELEMENT'
    compare_002.operation = 'EQUAL'
    # B
    compare_002.inputs[1].default_value = 0

    # Node Domain Size
    domain_size = spline_raycast_nodes_1.nodes.new("GeometryNodeAttributeDomainSize")
    domain_size.name = "Domain Size"
    domain_size.show_options = True
    domain_size.component = 'CURVE'

    # Node Domain Size.001
    domain_size_001 = spline_raycast_nodes_1.nodes.new("GeometryNodeAttributeDomainSize")
    domain_size_001.name = "Domain Size.001"
    domain_size_001.show_options = True
    domain_size_001.component = 'CURVE'

    # Node Points.001
    points_001 = spline_raycast_nodes_1.nodes.new("GeometryNodePoints")
    points_001.name = "Points.001"
    points_001.show_options = True

    # Node Sample Index.003
    sample_index_003 = spline_raycast_nodes_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_003.name = "Sample Index.003"
    sample_index_003.show_options = True
    sample_index_003.clamp = False
    sample_index_003.data_type = 'FLOAT_VECTOR'
    sample_index_003.domain = 'POINT'

    # Node Position.001
    position_001 = spline_raycast_nodes_1.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"
    position_001.show_options = True

    # Node Index.002
    index_002 = spline_raycast_nodes_1.nodes.new("GeometryNodeInputIndex")
    index_002.name = "Index.002"
    index_002.show_options = True

    # Node Points.002
    points_002 = spline_raycast_nodes_1.nodes.new("GeometryNodePoints")
    points_002.name = "Points.002"
    points_002.show_options = True

    # Node Sample Index.004
    sample_index_004 = spline_raycast_nodes_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_004.name = "Sample Index.004"
    sample_index_004.show_options = True
    sample_index_004.clamp = False
    sample_index_004.data_type = 'FLOAT_VECTOR'
    sample_index_004.domain = 'POINT'

    # Node Position.003
    position_003 = spline_raycast_nodes_1.nodes.new("GeometryNodeInputPosition")
    position_003.name = "Position.003"
    position_003.show_options = True

    # Node Index.003
    index_003 = spline_raycast_nodes_1.nodes.new("GeometryNodeInputIndex")
    index_003.name = "Index.003"
    index_003.show_options = True

    # Node Join Geometry.002
    join_geometry_002 = spline_raycast_nodes_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_002.name = "Join Geometry.002"
    join_geometry_002.show_options = True

    # Node Store Named Attribute.005
    store_named_attribute_005 = spline_raycast_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_005.name = "Store Named Attribute.005"
    store_named_attribute_005.show_options = True
    store_named_attribute_005.data_type = 'INT'
    store_named_attribute_005.domain = 'POINT'
    # Selection
    store_named_attribute_005.inputs[1].default_value = True
    # Name
    store_named_attribute_005.inputs[2].default_value = "cu_group"
    # Value
    store_named_attribute_005.inputs[3].default_value = 0

    # Node Sample Index.005
    sample_index_005 = spline_raycast_nodes_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_005.name = "Sample Index.005"
    sample_index_005.show_options = True
    sample_index_005.clamp = False
    sample_index_005.data_type = 'INT'
    sample_index_005.domain = 'POINT'

    # Node Sample Index.006
    sample_index_006 = spline_raycast_nodes_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_006.name = "Sample Index.006"
    sample_index_006.show_options = True
    sample_index_006.clamp = False
    sample_index_006.data_type = 'INT'
    sample_index_006.domain = 'POINT'

    # Node Named Attribute.007
    named_attribute_007 = spline_raycast_nodes_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_007.name = "Named Attribute.007"
    named_attribute_007.show_options = True
    named_attribute_007.data_type = 'FLOAT'
    # Name
    named_attribute_007.inputs[0].default_value = "radius"

    # Node Store Named Attribute.006
    store_named_attribute_006 = spline_raycast_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_006.name = "Store Named Attribute.006"
    store_named_attribute_006.show_options = True
    store_named_attribute_006.data_type = 'INT'
    store_named_attribute_006.domain = 'POINT'
    # Selection
    store_named_attribute_006.inputs[1].default_value = True
    # Name
    store_named_attribute_006.inputs[2].default_value = "curve_index"

    # Node Curve of Point.003
    curve_of_point_003 = spline_raycast_nodes_1.nodes.new("GeometryNodeCurveOfPoint")
    curve_of_point_003.name = "Curve of Point.003"
    curve_of_point_003.show_options = True
    # Point Index
    curve_of_point_003.inputs[0].default_value = 0

    # Node Named Attribute.008
    named_attribute_008 = spline_raycast_nodes_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_008.name = "Named Attribute.008"
    named_attribute_008.show_options = True
    named_attribute_008.data_type = 'FLOAT'
    # Name
    named_attribute_008.inputs[0].default_value = "radius"

    # Node Named Attribute.009
    named_attribute_009 = spline_raycast_nodes_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_009.name = "Named Attribute.009"
    named_attribute_009.show_options = True
    named_attribute_009.data_type = 'INT'
    # Name
    named_attribute_009.inputs[0].default_value = "curve_index"

    # Node Sample Index.007
    sample_index_007 = spline_raycast_nodes_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_007.name = "Sample Index.007"
    sample_index_007.show_options = True
    sample_index_007.clamp = False
    sample_index_007.data_type = 'INT'
    sample_index_007.domain = 'CURVE'

    # Node Index.004
    index_004 = spline_raycast_nodes_1.nodes.new("GeometryNodeInputIndex")
    index_004.name = "Index.004"
    index_004.show_options = True

    # Node Switch
    switch = spline_raycast_nodes_1.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.show_options = True
    switch.input_type = 'GEOMETRY'

    # Node Compare.007
    compare_007 = spline_raycast_nodes_1.nodes.new("FunctionNodeCompare")
    compare_007.name = "Compare.007"
    compare_007.show_options = True
    compare_007.data_type = 'INT'
    compare_007.mode = 'ELEMENT'
    compare_007.operation = 'GREATER_THAN'
    # B
    compare_007.inputs[1].default_value = 0

    # Node Separate Components
    separate_components = spline_raycast_nodes_1.nodes.new("GeometryNodeSeparateComponents")
    separate_components.name = "Separate Components"
    separate_components.show_options = True

    # Node Join Geometry.003
    join_geometry_003 = spline_raycast_nodes_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_003.name = "Join Geometry.003"
    join_geometry_003.show_options = True

    # Process zone input For Each Geometry Element Input
    for_each_geometry_element_input.pair_with_output(for_each_geometry_element_output)
    # Selection
    for_each_geometry_element_input.inputs[1].default_value = True



    # Set locations
    spline_raycast_nodes_1.nodes["Group Input"].location = (-1053.1202392578125, 26.092500686645508)
    spline_raycast_nodes_1.nodes["Group Output"].location = (7357.8486328125, 473.12115478515625)
    spline_raycast_nodes_1.nodes["Offset Point in Curve"].location = (-369.2333068847656, -429.2154541015625)
    spline_raycast_nodes_1.nodes["Sample Index"].location = (-163.80276489257812, -199.2880096435547)
    spline_raycast_nodes_1.nodes["Position"].location = (-373.6148376464844, -346.5038757324219)
    spline_raycast_nodes_1.nodes["Raycast"].location = (459.3544921875, -88.29640197753906)
    spline_raycast_nodes_1.nodes["Object Info"].location = (-712.6951904296875, 229.88101196289062)
    spline_raycast_nodes_1.nodes["Store Named Attribute.001"].location = (1078.3697509765625, 84.50520324707031)
    spline_raycast_nodes_1.nodes["Vector Math"].location = (178.10186767578125, -392.57220458984375)
    spline_raycast_nodes_1.nodes["Vector Math.001"].location = (377.77655029296875, -446.6107177734375)
    spline_raycast_nodes_1.nodes["Boolean Math"].location = (680.3968505859375, 4.2791748046875)
    spline_raycast_nodes_1.nodes["Store Named Attribute.003"].location = (1697.1163330078125, 174.15029907226562)
    spline_raycast_nodes_1.nodes["Accumulate Field"].location = (1531.0916748046875, 24.204254150390625)
    spline_raycast_nodes_1.nodes["Curve of Point.001"].location = (1353.130615234375, -150.89498901367188)
    spline_raycast_nodes_1.nodes["Named Attribute.001"].location = (1354.114501953125, -18.902938842773438)
    spline_raycast_nodes_1.nodes["Join Geometry"].location = (7086.8154296875, -75.73029327392578)
    spline_raycast_nodes_1.nodes["Spline Length"].location = (718.7775268554688, -369.91949462890625)
    spline_raycast_nodes_1.nodes["Math"].location = (880.2483520507812, -247.1407470703125)
    spline_raycast_nodes_1.nodes["Math.001"].location = (1038.72900390625, -118.37279510498047)
    spline_raycast_nodes_1.nodes["Spline Parameter"].location = (874.300537109375, -145.33065795898438)
    spline_raycast_nodes_1.nodes["Store Named Attribute.002"].location = (880.7826538085938, 283.8970947265625)
    spline_raycast_nodes_1.nodes["Mesh Island.001"].location = (259.6398620605469, -249.3448028564453)
    spline_raycast_nodes_1.nodes["Integer Math"].location = (683.8489990234375, 148.6571044921875)
    spline_raycast_nodes_1.nodes["Store Named Attribute.004"].location = (1948.8292236328125, 176.92044067382812)
    spline_raycast_nodes_1.nodes["Accumulate Field.002"].location = (1781.96435546875, 2.8723793029785156)
    spline_raycast_nodes_1.nodes["Named Attribute"].location = (1621.837158203125, -195.76614379882812)
    spline_raycast_nodes_1.nodes["Split to Instances.001"].location = (2705.1611328125, 1350.389892578125)
    spline_raycast_nodes_1.nodes["Compare.003"].location = (2532.229736328125, 1507.50732421875)
    spline_raycast_nodes_1.nodes["Named Attribute.004"].location = (2355.644775390625, 1326.406005859375)
    spline_raycast_nodes_1.nodes["For Each Geometry Element Input"].location = (3061.99755859375, 1438.731201171875)
    spline_raycast_nodes_1.nodes["For Each Geometry Element Output"].location = (6895.7421875, 1418.0804443359375)
    spline_raycast_nodes_1.nodes["Realize Instances"].location = (3292.0244140625, 1449.7269287109375)
    spline_raycast_nodes_1.nodes["Set Position.003"].location = (4532.736328125, 1471.31591796875)
    spline_raycast_nodes_1.nodes["Boolean Math.002"].location = (4105.83984375, 1613.00927734375)
    spline_raycast_nodes_1.nodes["Compare.004"].location = (3870.880615234375, 1769.860107421875)
    spline_raycast_nodes_1.nodes["Named Attribute.005"].location = (3668.640869140625, 1762.2152099609375)
    spline_raycast_nodes_1.nodes["Compare.005"].location = (3868.114501953125, 1609.1953125)
    spline_raycast_nodes_1.nodes["Spline Parameter.002"].location = (3669.870361328125, 1612.5789794921875)
    spline_raycast_nodes_1.nodes["Accumulate Field.003"].location = (3682.303955078125, 1324.9923095703125)
    spline_raycast_nodes_1.nodes["Curve of Point.002"].location = (3486.161376953125, 1174.5701904296875)
    spline_raycast_nodes_1.nodes["Position.002"].location = (3478.48583984375, 1246.3155517578125)
    spline_raycast_nodes_1.nodes["Vector Math.005"].location = (3875.063720703125, 1289.875244140625)
    spline_raycast_nodes_1.nodes["Domain Size.002"].location = (3499.3876953125, 1054.8475341796875)
    spline_raycast_nodes_1.nodes["Math.003"].location = (3690.451904296875, 1103.997802734375)
    spline_raycast_nodes_1.nodes["Vector Math.006"].location = (4041.737060546875, 1361.616943359375)
    spline_raycast_nodes_1.nodes["Vector Math.007"].location = (4301.74365234375, 1397.628173828125)
    spline_raycast_nodes_1.nodes["Map Range.001"].location = (4307.27490234375, 1239.732666015625)
    spline_raycast_nodes_1.nodes["Separate Geometry.001"].location = (2386.838623046875, -79.65594482421875)
    spline_raycast_nodes_1.nodes["Compare.006"].location = (2179.479736328125, 520.8291015625)
    spline_raycast_nodes_1.nodes["Named Attribute.006"].location = (1979.913818359375, 490.0750427246094)
    spline_raycast_nodes_1.nodes["Group Input.001"].location = (2429.833740234375, 917.135498046875)
    spline_raycast_nodes_1.nodes["Object Info.001"].location = (2614.78515625, 1001.457275390625)
    spline_raycast_nodes_1.nodes["Compare"].location = (3454.69482421875, 368.1105041503906)
    spline_raycast_nodes_1.nodes["Mesh Island"].location = (3094.4033203125, 298.2463073730469)
    spline_raycast_nodes_1.nodes["Mesh to Curve"].location = (3901.52685546875, 474.56793212890625)
    spline_raycast_nodes_1.nodes["Is Edge Loose"].location = (3243.12109375, 204.36587524414062)
    spline_raycast_nodes_1.nodes["Boolean Math.001"].location = (3708.978515625, 331.1709899902344)
    spline_raycast_nodes_1.nodes["Join Geometry.001"].location = (6661.10791015625, 1023.337890625)
    spline_raycast_nodes_1.nodes["Integer Math.001"].location = (3274.84521484375, 347.1900939941406)
    spline_raycast_nodes_1.nodes["Store Named Attribute"].location = (2972.808837890625, 972.8980102539062)
    spline_raycast_nodes_1.nodes["Vertex Neighbors"].location = (2628.558349609375, 723.7326049804688)
    spline_raycast_nodes_1.nodes["Compare.001"].location = (2803.763916015625, 814.1884155273438)
    spline_raycast_nodes_1.nodes["Reverse Curve"].location = (4388.76904296875, 473.52301025390625)
    spline_raycast_nodes_1.nodes["Points of Curve"].location = (3902.166015625, 213.17990112304688)
    spline_raycast_nodes_1.nodes["Sample Index.001"].location = (4081.02099609375, 416.62310791015625)
    spline_raycast_nodes_1.nodes["Named Attribute.002"].location = (3902.166015625, 345.8601989746094)
    spline_raycast_nodes_1.nodes["Boolean Math.003"].location = (4231.173828125, 419.01336669921875)
    spline_raycast_nodes_1.nodes["Points"].location = (3956.88916015625, 941.4781494140625)
    spline_raycast_nodes_1.nodes["Sample Index.002"].location = (3354.72998046875, 760.4039306640625)
    spline_raycast_nodes_1.nodes["Index"].location = (3172.936767578125, 590.6358032226562)
    spline_raycast_nodes_1.nodes["Sample Curve"].location = (3748.604736328125, 871.9004516601562)
    spline_raycast_nodes_1.nodes["Named Attribute.003"].location = (3022.788330078125, 722.18017578125)
    spline_raycast_nodes_1.nodes["Index.001"].location = (3574.859619140625, 625.1932373046875)
    spline_raycast_nodes_1.nodes["Trim Curve.001"].location = (3954.159423828125, 799.9461669921875)
    spline_raycast_nodes_1.nodes["Interpolate Curves"].location = (4572.17724609375, 764.382568359375)
    spline_raycast_nodes_1.nodes["Points to Curves"].location = (6221.5302734375, 484.26715087890625)
    spline_raycast_nodes_1.nodes["Delete Geometry"].location = (5106.08447265625, 502.710693359375)
    spline_raycast_nodes_1.nodes["Curve of Point"].location = (4755.11181640625, 537.4323120117188)
    spline_raycast_nodes_1.nodes["Compare.002"].location = (4925.263671875, 410.77911376953125)
    spline_raycast_nodes_1.nodes["Domain Size"].location = (5298.48193359375, 535.8196411132812)
    spline_raycast_nodes_1.nodes["Domain Size.001"].location = (5295.8583984375, 1084.308349609375)
    spline_raycast_nodes_1.nodes["Points.001"].location = (5640.5078125, 1085.208984375)
    spline_raycast_nodes_1.nodes["Sample Index.003"].location = (5467.20703125, 997.401611328125)
    spline_raycast_nodes_1.nodes["Position.001"].location = (5283.6533203125, 923.7041015625)
    spline_raycast_nodes_1.nodes["Index.002"].location = (5286.7216796875, 855.20751953125)
    spline_raycast_nodes_1.nodes["Points.002"].location = (5627.46435546875, 497.5929870605469)
    spline_raycast_nodes_1.nodes["Sample Index.004"].location = (5454.634765625, 355.5334167480469)
    spline_raycast_nodes_1.nodes["Position.003"].location = (5252.45654296875, 290.2186584472656)
    spline_raycast_nodes_1.nodes["Index.003"].location = (5261.10498046875, 199.36807250976562)
    spline_raycast_nodes_1.nodes["Join Geometry.002"].location = (6010.884765625, 659.550537109375)
    spline_raycast_nodes_1.nodes["Store Named Attribute.005"].location = (5808.7919921875, 902.8251953125)
    spline_raycast_nodes_1.nodes["Sample Index.005"].location = (5470.4677734375, 802.2515869140625)
    spline_raycast_nodes_1.nodes["Sample Index.006"].location = (5455.2236328125, 141.1004638671875)
    spline_raycast_nodes_1.nodes["Named Attribute.007"].location = (5980.1435546875, 355.1416015625)
    spline_raycast_nodes_1.nodes["Store Named Attribute.006"].location = (4345.45068359375, 681.822998046875)
    spline_raycast_nodes_1.nodes["Curve of Point.003"].location = (3524.23388671875, 535.5178833007812)
    spline_raycast_nodes_1.nodes["Named Attribute.008"].location = (4117.56982421875, 575.1054077148438)
    spline_raycast_nodes_1.nodes["Named Attribute.009"].location = (5153.0234375, 41.66281509399414)
    spline_raycast_nodes_1.nodes["Sample Index.007"].location = (3339.44970703125, 571.693115234375)
    spline_raycast_nodes_1.nodes["Index.004"].location = (3158.611572265625, 480.6488952636719)
    spline_raycast_nodes_1.nodes["Switch"].location = (6287.7763671875, 1155.35791015625)
    spline_raycast_nodes_1.nodes["Compare.007"].location = (6108.02294921875, 1254.91015625)
    spline_raycast_nodes_1.nodes["Separate Components"].location = (-828.830322265625, -94.28103637695312)
    spline_raycast_nodes_1.nodes["Join Geometry.003"].location = (-624.895263671875, -249.04171752929688)

    # Set dimensions
    spline_raycast_nodes_1.nodes["Group Input"].width  = 140.0
    spline_raycast_nodes_1.nodes["Group Input"].height = 100.0

    spline_raycast_nodes_1.nodes["Group Output"].width  = 140.0
    spline_raycast_nodes_1.nodes["Group Output"].height = 100.0

    spline_raycast_nodes_1.nodes["Offset Point in Curve"].width  = 160.0
    spline_raycast_nodes_1.nodes["Offset Point in Curve"].height = 100.0

    spline_raycast_nodes_1.nodes["Sample Index"].width  = 140.0
    spline_raycast_nodes_1.nodes["Sample Index"].height = 100.0

    spline_raycast_nodes_1.nodes["Position"].width  = 140.0
    spline_raycast_nodes_1.nodes["Position"].height = 100.0

    spline_raycast_nodes_1.nodes["Raycast"].width  = 160.0
    spline_raycast_nodes_1.nodes["Raycast"].height = 100.0

    spline_raycast_nodes_1.nodes["Object Info"].width  = 140.0
    spline_raycast_nodes_1.nodes["Object Info"].height = 100.0

    spline_raycast_nodes_1.nodes["Store Named Attribute.001"].width  = 160.0
    spline_raycast_nodes_1.nodes["Store Named Attribute.001"].height = 100.0

    spline_raycast_nodes_1.nodes["Vector Math"].width  = 140.0
    spline_raycast_nodes_1.nodes["Vector Math"].height = 100.0

    spline_raycast_nodes_1.nodes["Vector Math.001"].width  = 140.0
    spline_raycast_nodes_1.nodes["Vector Math.001"].height = 100.0

    spline_raycast_nodes_1.nodes["Boolean Math"].width  = 140.0
    spline_raycast_nodes_1.nodes["Boolean Math"].height = 100.0

    spline_raycast_nodes_1.nodes["Store Named Attribute.003"].width  = 160.0
    spline_raycast_nodes_1.nodes["Store Named Attribute.003"].height = 100.0

    spline_raycast_nodes_1.nodes["Accumulate Field"].width  = 140.0
    spline_raycast_nodes_1.nodes["Accumulate Field"].height = 100.0

    spline_raycast_nodes_1.nodes["Curve of Point.001"].width  = 140.0
    spline_raycast_nodes_1.nodes["Curve of Point.001"].height = 100.0

    spline_raycast_nodes_1.nodes["Named Attribute.001"].width  = 140.0
    spline_raycast_nodes_1.nodes["Named Attribute.001"].height = 100.0

    spline_raycast_nodes_1.nodes["Join Geometry"].width  = 140.0
    spline_raycast_nodes_1.nodes["Join Geometry"].height = 100.0

    spline_raycast_nodes_1.nodes["Spline Length"].width  = 140.0
    spline_raycast_nodes_1.nodes["Spline Length"].height = 100.0

    spline_raycast_nodes_1.nodes["Math"].width  = 140.0
    spline_raycast_nodes_1.nodes["Math"].height = 100.0

    spline_raycast_nodes_1.nodes["Math.001"].width  = 140.0
    spline_raycast_nodes_1.nodes["Math.001"].height = 100.0

    spline_raycast_nodes_1.nodes["Spline Parameter"].width  = 140.0
    spline_raycast_nodes_1.nodes["Spline Parameter"].height = 100.0

    spline_raycast_nodes_1.nodes["Store Named Attribute.002"].width  = 160.0
    spline_raycast_nodes_1.nodes["Store Named Attribute.002"].height = 100.0

    spline_raycast_nodes_1.nodes["Mesh Island.001"].width  = 140.0
    spline_raycast_nodes_1.nodes["Mesh Island.001"].height = 100.0

    spline_raycast_nodes_1.nodes["Integer Math"].width  = 140.0
    spline_raycast_nodes_1.nodes["Integer Math"].height = 100.0

    spline_raycast_nodes_1.nodes["Store Named Attribute.004"].width  = 160.0
    spline_raycast_nodes_1.nodes["Store Named Attribute.004"].height = 100.0

    spline_raycast_nodes_1.nodes["Accumulate Field.002"].width  = 140.0
    spline_raycast_nodes_1.nodes["Accumulate Field.002"].height = 100.0

    spline_raycast_nodes_1.nodes["Named Attribute"].width  = 140.0
    spline_raycast_nodes_1.nodes["Named Attribute"].height = 100.0

    spline_raycast_nodes_1.nodes["Split to Instances.001"].width  = 140.0
    spline_raycast_nodes_1.nodes["Split to Instances.001"].height = 100.0

    spline_raycast_nodes_1.nodes["Compare.003"].width  = 140.0
    spline_raycast_nodes_1.nodes["Compare.003"].height = 100.0

    spline_raycast_nodes_1.nodes["Named Attribute.004"].width  = 140.0
    spline_raycast_nodes_1.nodes["Named Attribute.004"].height = 100.0

    spline_raycast_nodes_1.nodes["For Each Geometry Element Input"].width  = 170.16162109375
    spline_raycast_nodes_1.nodes["For Each Geometry Element Input"].height = 100.0

    spline_raycast_nodes_1.nodes["For Each Geometry Element Output"].width  = 140.0
    spline_raycast_nodes_1.nodes["For Each Geometry Element Output"].height = 100.0

    spline_raycast_nodes_1.nodes["Realize Instances"].width  = 140.0
    spline_raycast_nodes_1.nodes["Realize Instances"].height = 100.0

    spline_raycast_nodes_1.nodes["Set Position.003"].width  = 140.0
    spline_raycast_nodes_1.nodes["Set Position.003"].height = 100.0

    spline_raycast_nodes_1.nodes["Boolean Math.002"].width  = 140.0
    spline_raycast_nodes_1.nodes["Boolean Math.002"].height = 100.0

    spline_raycast_nodes_1.nodes["Compare.004"].width  = 140.0
    spline_raycast_nodes_1.nodes["Compare.004"].height = 100.0

    spline_raycast_nodes_1.nodes["Named Attribute.005"].width  = 140.0
    spline_raycast_nodes_1.nodes["Named Attribute.005"].height = 100.0

    spline_raycast_nodes_1.nodes["Compare.005"].width  = 140.0
    spline_raycast_nodes_1.nodes["Compare.005"].height = 100.0

    spline_raycast_nodes_1.nodes["Spline Parameter.002"].width  = 140.0
    spline_raycast_nodes_1.nodes["Spline Parameter.002"].height = 100.0

    spline_raycast_nodes_1.nodes["Accumulate Field.003"].width  = 140.0
    spline_raycast_nodes_1.nodes["Accumulate Field.003"].height = 100.0

    spline_raycast_nodes_1.nodes["Curve of Point.002"].width  = 140.0
    spline_raycast_nodes_1.nodes["Curve of Point.002"].height = 100.0

    spline_raycast_nodes_1.nodes["Position.002"].width  = 140.0
    spline_raycast_nodes_1.nodes["Position.002"].height = 100.0

    spline_raycast_nodes_1.nodes["Vector Math.005"].width  = 140.0
    spline_raycast_nodes_1.nodes["Vector Math.005"].height = 100.0

    spline_raycast_nodes_1.nodes["Domain Size.002"].width  = 140.0
    spline_raycast_nodes_1.nodes["Domain Size.002"].height = 100.0

    spline_raycast_nodes_1.nodes["Math.003"].width  = 140.0
    spline_raycast_nodes_1.nodes["Math.003"].height = 100.0

    spline_raycast_nodes_1.nodes["Vector Math.006"].width  = 140.0
    spline_raycast_nodes_1.nodes["Vector Math.006"].height = 100.0

    spline_raycast_nodes_1.nodes["Vector Math.007"].width  = 140.0
    spline_raycast_nodes_1.nodes["Vector Math.007"].height = 100.0

    spline_raycast_nodes_1.nodes["Map Range.001"].width  = 140.0
    spline_raycast_nodes_1.nodes["Map Range.001"].height = 100.0

    spline_raycast_nodes_1.nodes["Separate Geometry.001"].width  = 140.0
    spline_raycast_nodes_1.nodes["Separate Geometry.001"].height = 100.0

    spline_raycast_nodes_1.nodes["Compare.006"].width  = 140.0
    spline_raycast_nodes_1.nodes["Compare.006"].height = 100.0

    spline_raycast_nodes_1.nodes["Named Attribute.006"].width  = 140.0
    spline_raycast_nodes_1.nodes["Named Attribute.006"].height = 100.0

    spline_raycast_nodes_1.nodes["Group Input.001"].width  = 140.0
    spline_raycast_nodes_1.nodes["Group Input.001"].height = 100.0

    spline_raycast_nodes_1.nodes["Object Info.001"].width  = 140.0
    spline_raycast_nodes_1.nodes["Object Info.001"].height = 100.0

    spline_raycast_nodes_1.nodes["Compare"].width  = 140.0
    spline_raycast_nodes_1.nodes["Compare"].height = 100.0

    spline_raycast_nodes_1.nodes["Mesh Island"].width  = 140.0
    spline_raycast_nodes_1.nodes["Mesh Island"].height = 100.0

    spline_raycast_nodes_1.nodes["Mesh to Curve"].width  = 140.0
    spline_raycast_nodes_1.nodes["Mesh to Curve"].height = 100.0

    spline_raycast_nodes_1.nodes["Is Edge Loose"].width  = 140.0
    spline_raycast_nodes_1.nodes["Is Edge Loose"].height = 100.0

    spline_raycast_nodes_1.nodes["Boolean Math.001"].width  = 140.0
    spline_raycast_nodes_1.nodes["Boolean Math.001"].height = 100.0

    spline_raycast_nodes_1.nodes["Join Geometry.001"].width  = 140.0
    spline_raycast_nodes_1.nodes["Join Geometry.001"].height = 100.0

    spline_raycast_nodes_1.nodes["Integer Math.001"].width  = 140.0
    spline_raycast_nodes_1.nodes["Integer Math.001"].height = 100.0

    spline_raycast_nodes_1.nodes["Store Named Attribute"].width  = 160.0
    spline_raycast_nodes_1.nodes["Store Named Attribute"].height = 100.0

    spline_raycast_nodes_1.nodes["Vertex Neighbors"].width  = 140.0
    spline_raycast_nodes_1.nodes["Vertex Neighbors"].height = 100.0

    spline_raycast_nodes_1.nodes["Compare.001"].width  = 140.0
    spline_raycast_nodes_1.nodes["Compare.001"].height = 100.0

    spline_raycast_nodes_1.nodes["Reverse Curve"].width  = 140.0
    spline_raycast_nodes_1.nodes["Reverse Curve"].height = 100.0

    spline_raycast_nodes_1.nodes["Points of Curve"].width  = 140.0
    spline_raycast_nodes_1.nodes["Points of Curve"].height = 100.0

    spline_raycast_nodes_1.nodes["Sample Index.001"].width  = 140.0
    spline_raycast_nodes_1.nodes["Sample Index.001"].height = 100.0

    spline_raycast_nodes_1.nodes["Named Attribute.002"].width  = 140.0
    spline_raycast_nodes_1.nodes["Named Attribute.002"].height = 100.0

    spline_raycast_nodes_1.nodes["Boolean Math.003"].width  = 140.0
    spline_raycast_nodes_1.nodes["Boolean Math.003"].height = 100.0

    spline_raycast_nodes_1.nodes["Points"].width  = 140.0
    spline_raycast_nodes_1.nodes["Points"].height = 100.0

    spline_raycast_nodes_1.nodes["Sample Index.002"].width  = 140.0
    spline_raycast_nodes_1.nodes["Sample Index.002"].height = 100.0

    spline_raycast_nodes_1.nodes["Index"].width  = 140.0
    spline_raycast_nodes_1.nodes["Index"].height = 100.0

    spline_raycast_nodes_1.nodes["Sample Curve"].width  = 140.0
    spline_raycast_nodes_1.nodes["Sample Curve"].height = 100.0

    spline_raycast_nodes_1.nodes["Named Attribute.003"].width  = 140.0
    spline_raycast_nodes_1.nodes["Named Attribute.003"].height = 100.0

    spline_raycast_nodes_1.nodes["Index.001"].width  = 140.0
    spline_raycast_nodes_1.nodes["Index.001"].height = 100.0

    spline_raycast_nodes_1.nodes["Trim Curve.001"].width  = 140.0
    spline_raycast_nodes_1.nodes["Trim Curve.001"].height = 100.0

    spline_raycast_nodes_1.nodes["Interpolate Curves"].width  = 140.0
    spline_raycast_nodes_1.nodes["Interpolate Curves"].height = 100.0

    spline_raycast_nodes_1.nodes["Points to Curves"].width  = 140.0
    spline_raycast_nodes_1.nodes["Points to Curves"].height = 100.0

    spline_raycast_nodes_1.nodes["Delete Geometry"].width  = 140.0
    spline_raycast_nodes_1.nodes["Delete Geometry"].height = 100.0

    spline_raycast_nodes_1.nodes["Curve of Point"].width  = 140.0
    spline_raycast_nodes_1.nodes["Curve of Point"].height = 100.0

    spline_raycast_nodes_1.nodes["Compare.002"].width  = 140.0
    spline_raycast_nodes_1.nodes["Compare.002"].height = 100.0

    spline_raycast_nodes_1.nodes["Domain Size"].width  = 140.0
    spline_raycast_nodes_1.nodes["Domain Size"].height = 100.0

    spline_raycast_nodes_1.nodes["Domain Size.001"].width  = 140.0
    spline_raycast_nodes_1.nodes["Domain Size.001"].height = 100.0

    spline_raycast_nodes_1.nodes["Points.001"].width  = 140.0
    spline_raycast_nodes_1.nodes["Points.001"].height = 100.0

    spline_raycast_nodes_1.nodes["Sample Index.003"].width  = 140.0
    spline_raycast_nodes_1.nodes["Sample Index.003"].height = 100.0

    spline_raycast_nodes_1.nodes["Position.001"].width  = 140.0
    spline_raycast_nodes_1.nodes["Position.001"].height = 100.0

    spline_raycast_nodes_1.nodes["Index.002"].width  = 140.0
    spline_raycast_nodes_1.nodes["Index.002"].height = 100.0

    spline_raycast_nodes_1.nodes["Points.002"].width  = 140.0
    spline_raycast_nodes_1.nodes["Points.002"].height = 100.0

    spline_raycast_nodes_1.nodes["Sample Index.004"].width  = 140.0
    spline_raycast_nodes_1.nodes["Sample Index.004"].height = 100.0

    spline_raycast_nodes_1.nodes["Position.003"].width  = 140.0
    spline_raycast_nodes_1.nodes["Position.003"].height = 100.0

    spline_raycast_nodes_1.nodes["Index.003"].width  = 140.0
    spline_raycast_nodes_1.nodes["Index.003"].height = 100.0

    spline_raycast_nodes_1.nodes["Join Geometry.002"].width  = 140.0
    spline_raycast_nodes_1.nodes["Join Geometry.002"].height = 100.0

    spline_raycast_nodes_1.nodes["Store Named Attribute.005"].width  = 160.0
    spline_raycast_nodes_1.nodes["Store Named Attribute.005"].height = 100.0

    spline_raycast_nodes_1.nodes["Sample Index.005"].width  = 140.0
    spline_raycast_nodes_1.nodes["Sample Index.005"].height = 100.0

    spline_raycast_nodes_1.nodes["Sample Index.006"].width  = 140.0
    spline_raycast_nodes_1.nodes["Sample Index.006"].height = 100.0

    spline_raycast_nodes_1.nodes["Named Attribute.007"].width  = 140.0
    spline_raycast_nodes_1.nodes["Named Attribute.007"].height = 100.0

    spline_raycast_nodes_1.nodes["Store Named Attribute.006"].width  = 160.0
    spline_raycast_nodes_1.nodes["Store Named Attribute.006"].height = 100.0

    spline_raycast_nodes_1.nodes["Curve of Point.003"].width  = 140.0
    spline_raycast_nodes_1.nodes["Curve of Point.003"].height = 100.0

    spline_raycast_nodes_1.nodes["Named Attribute.008"].width  = 140.0
    spline_raycast_nodes_1.nodes["Named Attribute.008"].height = 100.0

    spline_raycast_nodes_1.nodes["Named Attribute.009"].width  = 140.0
    spline_raycast_nodes_1.nodes["Named Attribute.009"].height = 100.0

    spline_raycast_nodes_1.nodes["Sample Index.007"].width  = 140.0
    spline_raycast_nodes_1.nodes["Sample Index.007"].height = 100.0

    spline_raycast_nodes_1.nodes["Index.004"].width  = 140.0
    spline_raycast_nodes_1.nodes["Index.004"].height = 100.0

    spline_raycast_nodes_1.nodes["Switch"].width  = 140.0
    spline_raycast_nodes_1.nodes["Switch"].height = 100.0

    spline_raycast_nodes_1.nodes["Compare.007"].width  = 140.0
    spline_raycast_nodes_1.nodes["Compare.007"].height = 100.0

    spline_raycast_nodes_1.nodes["Separate Components"].width  = 160.0
    spline_raycast_nodes_1.nodes["Separate Components"].height = 100.0

    spline_raycast_nodes_1.nodes["Join Geometry.003"].width  = 140.0
    spline_raycast_nodes_1.nodes["Join Geometry.003"].height = 100.0


    # Initialize spline_raycast_nodes_1 links

    # join_geometry.Geometry -> group_output.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Join Geometry"].outputs[0],
        spline_raycast_nodes_1.nodes["Group Output"].inputs[0]
    )
    # offset_point_in_curve.Point Index -> sample_index.Index
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Offset Point in Curve"].outputs[1],
        spline_raycast_nodes_1.nodes["Sample Index"].inputs[2]
    )
    # position.Position -> sample_index.Value
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Position"].outputs[0],
        spline_raycast_nodes_1.nodes["Sample Index"].inputs[1]
    )
    # object_info.Geometry -> raycast.Target Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Object Info"].outputs[4],
        spline_raycast_nodes_1.nodes["Raycast"].inputs[0]
    )
    # vector_math.Vector -> vector_math_001.Vector
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Vector Math"].outputs[0],
        spline_raycast_nodes_1.nodes["Vector Math.001"].inputs[0]
    )
    # raycast.Is Hit -> boolean_math.Boolean
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Raycast"].outputs[0],
        spline_raycast_nodes_1.nodes["Boolean Math"].inputs[1]
    )
    # vector_math.Vector -> raycast.Ray Direction
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Vector Math"].outputs[0],
        spline_raycast_nodes_1.nodes["Raycast"].inputs[4]
    )
    # store_named_attribute_001.Geometry -> store_named_attribute_003.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Store Named Attribute.001"].outputs[0],
        spline_raycast_nodes_1.nodes["Store Named Attribute.003"].inputs[0]
    )
    # curve_of_point_001.Curve Index -> accumulate_field.Group ID
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Curve of Point.001"].outputs[0],
        spline_raycast_nodes_1.nodes["Accumulate Field"].inputs[1]
    )
    # named_attribute_001.Attribute -> accumulate_field.Value
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Named Attribute.001"].outputs[0],
        spline_raycast_nodes_1.nodes["Accumulate Field"].inputs[0]
    )
    # accumulate_field.Total -> store_named_attribute_003.Value
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Accumulate Field"].outputs[2],
        spline_raycast_nodes_1.nodes["Store Named Attribute.003"].inputs[3]
    )
    # offset_point_in_curve.Is Valid Offset -> boolean_math.Boolean
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Offset Point in Curve"].outputs[0],
        spline_raycast_nodes_1.nodes["Boolean Math"].inputs[0]
    )
    # spline_length.Length -> math.Value
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Spline Length"].outputs[0],
        spline_raycast_nodes_1.nodes["Math"].inputs[1]
    )
    # raycast.Hit Distance -> math.Value
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Raycast"].outputs[3],
        spline_raycast_nodes_1.nodes["Math"].inputs[0]
    )
    # spline_parameter.Factor -> math_001.Value
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Spline Parameter"].outputs[0],
        spline_raycast_nodes_1.nodes["Math.001"].inputs[0]
    )
    # math.Value -> math_001.Value
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Math"].outputs[0],
        spline_raycast_nodes_1.nodes["Math.001"].inputs[1]
    )
    # store_named_attribute_002.Geometry -> store_named_attribute_001.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Store Named Attribute.002"].outputs[0],
        spline_raycast_nodes_1.nodes["Store Named Attribute.001"].inputs[0]
    )
    # boolean_math.Boolean -> store_named_attribute_001.Selection
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Boolean Math"].outputs[0],
        spline_raycast_nodes_1.nodes["Store Named Attribute.001"].inputs[1]
    )
    # sample_index.Value -> vector_math.Vector
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Sample Index"].outputs[0],
        spline_raycast_nodes_1.nodes["Vector Math"].inputs[0]
    )
    # vector_math_001.Value -> raycast.Ray Length
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Vector Math.001"].outputs[1],
        spline_raycast_nodes_1.nodes["Raycast"].inputs[5]
    )
    # position.Position -> vector_math.Vector
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Position"].outputs[0],
        spline_raycast_nodes_1.nodes["Vector Math"].inputs[1]
    )
    # position.Position -> raycast.Source Position
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Position"].outputs[0],
        spline_raycast_nodes_1.nodes["Raycast"].inputs[3]
    )
    # math_001.Value -> store_named_attribute_001.Value
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Math.001"].outputs[0],
        spline_raycast_nodes_1.nodes["Store Named Attribute.001"].inputs[3]
    )
    # mesh_island_001.Island Index -> raycast.Attribute
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Mesh Island.001"].outputs[0],
        spline_raycast_nodes_1.nodes["Raycast"].inputs[1]
    )
    # raycast.Attribute -> integer_math.Value
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Raycast"].outputs[4],
        spline_raycast_nodes_1.nodes["Integer Math"].inputs[0]
    )
    # integer_math.Value -> store_named_attribute_002.Value
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Integer Math"].outputs[0],
        spline_raycast_nodes_1.nodes["Store Named Attribute.002"].inputs[3]
    )
    # boolean_math.Boolean -> store_named_attribute_002.Selection
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Boolean Math"].outputs[0],
        spline_raycast_nodes_1.nodes["Store Named Attribute.002"].inputs[1]
    )
    # store_named_attribute_003.Geometry -> store_named_attribute_004.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Store Named Attribute.003"].outputs[0],
        spline_raycast_nodes_1.nodes["Store Named Attribute.004"].inputs[0]
    )
    # accumulate_field_002.Total -> store_named_attribute_004.Value
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Accumulate Field.002"].outputs[2],
        spline_raycast_nodes_1.nodes["Store Named Attribute.004"].inputs[3]
    )
    # named_attribute.Attribute -> accumulate_field_002.Value
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Named Attribute"].outputs[0],
        spline_raycast_nodes_1.nodes["Accumulate Field.002"].inputs[0]
    )
    # curve_of_point_001.Curve Index -> accumulate_field_002.Group ID
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Curve of Point.001"].outputs[0],
        spline_raycast_nodes_1.nodes["Accumulate Field.002"].inputs[1]
    )
    # named_attribute_004.Attribute -> split_to_instances_001.Group ID
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Named Attribute.004"].outputs[0],
        spline_raycast_nodes_1.nodes["Split to Instances.001"].inputs[2]
    )
    # named_attribute_004.Attribute -> compare_003.A
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Named Attribute.004"].outputs[0],
        spline_raycast_nodes_1.nodes["Compare.003"].inputs[0]
    )
    # compare_003.Result -> split_to_instances_001.Selection
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Compare.003"].outputs[0],
        spline_raycast_nodes_1.nodes["Split to Instances.001"].inputs[1]
    )
    # split_to_instances_001.Instances -> for_each_geometry_element_input.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Split to Instances.001"].outputs[0],
        spline_raycast_nodes_1.nodes["For Each Geometry Element Input"].inputs[0]
    )
    # for_each_geometry_element_input.Element -> realize_instances.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["For Each Geometry Element Input"].outputs[1],
        spline_raycast_nodes_1.nodes["Realize Instances"].inputs[0]
    )
    # boolean_math_002.Boolean -> set_position_003.Selection
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Boolean Math.002"].outputs[0],
        spline_raycast_nodes_1.nodes["Set Position.003"].inputs[1]
    )
    # named_attribute_005.Attribute -> compare_004.A
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Named Attribute.005"].outputs[0],
        spline_raycast_nodes_1.nodes["Compare.004"].inputs[0]
    )
    # compare_004.Result -> boolean_math_002.Boolean
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Compare.004"].outputs[0],
        spline_raycast_nodes_1.nodes["Boolean Math.002"].inputs[0]
    )
    # spline_parameter_002.Factor -> compare_005.A
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Spline Parameter.002"].outputs[0],
        spline_raycast_nodes_1.nodes["Compare.005"].inputs[0]
    )
    # named_attribute_005.Attribute -> compare_005.B
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Named Attribute.005"].outputs[0],
        spline_raycast_nodes_1.nodes["Compare.005"].inputs[1]
    )
    # compare_005.Result -> boolean_math_002.Boolean
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Compare.005"].outputs[0],
        spline_raycast_nodes_1.nodes["Boolean Math.002"].inputs[1]
    )
    # curve_of_point_002.Index in Curve -> accumulate_field_003.Group ID
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Curve of Point.002"].outputs[1],
        spline_raycast_nodes_1.nodes["Accumulate Field.003"].inputs[1]
    )
    # position_002.Position -> accumulate_field_003.Value
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Position.002"].outputs[0],
        spline_raycast_nodes_1.nodes["Accumulate Field.003"].inputs[0]
    )
    # accumulate_field_003.Total -> vector_math_005.Vector
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Accumulate Field.003"].outputs[2],
        spline_raycast_nodes_1.nodes["Vector Math.005"].inputs[0]
    )
    # vector_math_005.Vector -> vector_math_006.Vector
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Vector Math.005"].outputs[0],
        spline_raycast_nodes_1.nodes["Vector Math.006"].inputs[0]
    )
    # position_002.Position -> vector_math_006.Vector
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Position.002"].outputs[0],
        spline_raycast_nodes_1.nodes["Vector Math.006"].inputs[1]
    )
    # vector_math_006.Vector -> vector_math_007.Vector
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Vector Math.006"].outputs[0],
        spline_raycast_nodes_1.nodes["Vector Math.007"].inputs[0]
    )
    # map_range_001.Result -> vector_math_007.Scale
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Map Range.001"].outputs[0],
        spline_raycast_nodes_1.nodes["Vector Math.007"].inputs[3]
    )
    # spline_parameter_002.Factor -> map_range_001.Value
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Spline Parameter.002"].outputs[0],
        spline_raycast_nodes_1.nodes["Map Range.001"].inputs[0]
    )
    # named_attribute_005.Attribute -> map_range_001.From Min
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Named Attribute.005"].outputs[0],
        spline_raycast_nodes_1.nodes["Map Range.001"].inputs[1]
    )
    # domain_size_002.Spline Count -> math_003.Value
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Domain Size.002"].outputs[4],
        spline_raycast_nodes_1.nodes["Math.003"].inputs[1]
    )
    # math_003.Value -> vector_math_005.Scale
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Math.003"].outputs[0],
        spline_raycast_nodes_1.nodes["Vector Math.005"].inputs[3]
    )
    # vector_math_007.Vector -> set_position_003.Offset
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Vector Math.007"].outputs[0],
        spline_raycast_nodes_1.nodes["Set Position.003"].inputs[3]
    )
    # realize_instances.Geometry -> set_position_003.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Realize Instances"].outputs[0],
        spline_raycast_nodes_1.nodes["Set Position.003"].inputs[0]
    )
    # join_geometry_001.Geometry -> for_each_geometry_element_output.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Join Geometry.001"].outputs[0],
        spline_raycast_nodes_1.nodes["For Each Geometry Element Output"].inputs[1]
    )
    # realize_instances.Geometry -> domain_size_002.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Realize Instances"].outputs[0],
        spline_raycast_nodes_1.nodes["Domain Size.002"].inputs[0]
    )
    # named_attribute_006.Attribute -> compare_006.A
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Named Attribute.006"].outputs[0],
        spline_raycast_nodes_1.nodes["Compare.006"].inputs[0]
    )
    # compare_006.Result -> separate_geometry_001.Selection
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Compare.006"].outputs[0],
        spline_raycast_nodes_1.nodes["Separate Geometry.001"].inputs[1]
    )
    # store_named_attribute_004.Geometry -> separate_geometry_001.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Store Named Attribute.004"].outputs[0],
        spline_raycast_nodes_1.nodes["Separate Geometry.001"].inputs[0]
    )
    # separate_geometry_001.Selection -> split_to_instances_001.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Separate Geometry.001"].outputs[0],
        spline_raycast_nodes_1.nodes["Split to Instances.001"].inputs[0]
    )
    # group_input.Target Object -> object_info.Object
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Group Input"].outputs[1],
        spline_raycast_nodes_1.nodes["Object Info"].inputs[0]
    )
    # split_to_instances_001.Group ID -> for_each_geometry_element_input.Group ID
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Split to Instances.001"].outputs[1],
        spline_raycast_nodes_1.nodes["For Each Geometry Element Input"].inputs[2]
    )
    # group_input_001.Target Object -> object_info_001.Object
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Group Input.001"].outputs[1],
        spline_raycast_nodes_1.nodes["Object Info.001"].inputs[0]
    )
    # integer_math_001.Value -> compare.A
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Integer Math.001"].outputs[0],
        spline_raycast_nodes_1.nodes["Compare"].inputs[0]
    )
    # for_each_geometry_element_input.Group ID -> compare.B
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["For Each Geometry Element Input"].outputs[2],
        spline_raycast_nodes_1.nodes["Compare"].inputs[1]
    )
    # compare.Result -> boolean_math_001.Boolean
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Compare"].outputs[0],
        spline_raycast_nodes_1.nodes["Boolean Math.001"].inputs[0]
    )
    # store_named_attribute.Geometry -> mesh_to_curve.Mesh
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Store Named Attribute"].outputs[0],
        spline_raycast_nodes_1.nodes["Mesh to Curve"].inputs[0]
    )
    # is_edge_loose.Is Edge Loose -> boolean_math_001.Boolean
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Is Edge Loose"].outputs[0],
        spline_raycast_nodes_1.nodes["Boolean Math.001"].inputs[1]
    )
    # boolean_math_001.Boolean -> mesh_to_curve.Selection
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Boolean Math.001"].outputs[0],
        spline_raycast_nodes_1.nodes["Mesh to Curve"].inputs[1]
    )
    # mesh_island.Island Index -> integer_math_001.Value
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Mesh Island"].outputs[0],
        spline_raycast_nodes_1.nodes["Integer Math.001"].inputs[0]
    )
    # object_info_001.Geometry -> store_named_attribute.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Object Info.001"].outputs[4],
        spline_raycast_nodes_1.nodes["Store Named Attribute"].inputs[0]
    )
    # vertex_neighbors.Vertex Count -> compare_001.A
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Vertex Neighbors"].outputs[0],
        spline_raycast_nodes_1.nodes["Compare.001"].inputs[0]
    )
    # compare_001.Result -> store_named_attribute.Selection
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Compare.001"].outputs[0],
        spline_raycast_nodes_1.nodes["Store Named Attribute"].inputs[1]
    )
    # mesh_to_curve.Curve -> reverse_curve.Curve
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Mesh to Curve"].outputs[0],
        spline_raycast_nodes_1.nodes["Reverse Curve"].inputs[0]
    )
    # mesh_to_curve.Curve -> sample_index_001.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Mesh to Curve"].outputs[0],
        spline_raycast_nodes_1.nodes["Sample Index.001"].inputs[0]
    )
    # points_of_curve.Point Index -> sample_index_001.Index
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Points of Curve"].outputs[0],
        spline_raycast_nodes_1.nodes["Sample Index.001"].inputs[2]
    )
    # named_attribute_002.Attribute -> sample_index_001.Value
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Named Attribute.002"].outputs[0],
        spline_raycast_nodes_1.nodes["Sample Index.001"].inputs[1]
    )
    # sample_index_001.Value -> boolean_math_003.Boolean
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Sample Index.001"].outputs[0],
        spline_raycast_nodes_1.nodes["Boolean Math.003"].inputs[0]
    )
    # boolean_math_003.Boolean -> reverse_curve.Selection
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Boolean Math.003"].outputs[0],
        spline_raycast_nodes_1.nodes["Reverse Curve"].inputs[1]
    )
    # domain_size_002.Spline Count -> points.Count
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Domain Size.002"].outputs[4],
        spline_raycast_nodes_1.nodes["Points"].inputs[0]
    )
    # realize_instances.Geometry -> sample_index_002.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Realize Instances"].outputs[0],
        spline_raycast_nodes_1.nodes["Sample Index.002"].inputs[0]
    )
    # realize_instances.Geometry -> sample_curve.Curves
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Realize Instances"].outputs[0],
        spline_raycast_nodes_1.nodes["Sample Curve"].inputs[0]
    )
    # sample_curve.Position -> points.Position
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Sample Curve"].outputs[1],
        spline_raycast_nodes_1.nodes["Points"].inputs[1]
    )
    # index.Index -> sample_index_002.Index
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Index"].outputs[0],
        spline_raycast_nodes_1.nodes["Sample Index.002"].inputs[2]
    )
    # named_attribute_003.Attribute -> sample_index_002.Value
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Named Attribute.003"].outputs[0],
        spline_raycast_nodes_1.nodes["Sample Index.002"].inputs[1]
    )
    # sample_index_002.Value -> sample_curve.Factor
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Sample Index.002"].outputs[0],
        spline_raycast_nodes_1.nodes["Sample Curve"].inputs[2]
    )
    # index_001.Index -> sample_curve.Curve Index
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Index.001"].outputs[0],
        spline_raycast_nodes_1.nodes["Sample Curve"].inputs[4]
    )
    # realize_instances.Geometry -> trim_curve_001.Curve
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Realize Instances"].outputs[0],
        spline_raycast_nodes_1.nodes["Trim Curve.001"].inputs[0]
    )
    # named_attribute_003.Attribute -> trim_curve_001.End
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Named Attribute.003"].outputs[0],
        spline_raycast_nodes_1.nodes["Trim Curve.001"].inputs[3]
    )
    # store_named_attribute_006.Geometry -> interpolate_curves.Points
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Store Named Attribute.006"].outputs[0],
        spline_raycast_nodes_1.nodes["Interpolate Curves"].inputs[3]
    )
    # reverse_curve.Curve -> interpolate_curves.Guide Curves
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Reverse Curve"].outputs[0],
        spline_raycast_nodes_1.nodes["Interpolate Curves"].inputs[0]
    )
    # interpolate_curves.Curves -> delete_geometry.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Interpolate Curves"].outputs[0],
        spline_raycast_nodes_1.nodes["Delete Geometry"].inputs[0]
    )
    # compare_002.Result -> delete_geometry.Selection
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Compare.002"].outputs[0],
        spline_raycast_nodes_1.nodes["Delete Geometry"].inputs[1]
    )
    # delete_geometry.Geometry -> domain_size.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Delete Geometry"].outputs[0],
        spline_raycast_nodes_1.nodes["Domain Size"].inputs[0]
    )
    # domain_size_001.Point Count -> points_001.Count
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Domain Size.001"].outputs[0],
        spline_raycast_nodes_1.nodes["Points.001"].inputs[0]
    )
    # sample_index_003.Value -> points_001.Position
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Sample Index.003"].outputs[0],
        spline_raycast_nodes_1.nodes["Points.001"].inputs[1]
    )
    # position_001.Position -> sample_index_003.Value
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Position.001"].outputs[0],
        spline_raycast_nodes_1.nodes["Sample Index.003"].inputs[1]
    )
    # index_002.Index -> sample_index_003.Index
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Index.002"].outputs[0],
        spline_raycast_nodes_1.nodes["Sample Index.003"].inputs[2]
    )
    # domain_size.Point Count -> points_002.Count
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Domain Size"].outputs[0],
        spline_raycast_nodes_1.nodes["Points.002"].inputs[0]
    )
    # position_003.Position -> sample_index_004.Value
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Position.003"].outputs[0],
        spline_raycast_nodes_1.nodes["Sample Index.004"].inputs[1]
    )
    # index_003.Index -> sample_index_004.Index
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Index.003"].outputs[0],
        spline_raycast_nodes_1.nodes["Sample Index.004"].inputs[2]
    )
    # sample_index_004.Value -> points_002.Position
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Sample Index.004"].outputs[0],
        spline_raycast_nodes_1.nodes["Points.002"].inputs[1]
    )
    # points_001.Points -> store_named_attribute_005.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Points.001"].outputs[0],
        spline_raycast_nodes_1.nodes["Store Named Attribute.005"].inputs[0]
    )
    # index_002.Index -> sample_index_005.Index
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Index.002"].outputs[0],
        spline_raycast_nodes_1.nodes["Sample Index.005"].inputs[2]
    )
    # curve_of_point.Curve Index -> sample_index_005.Value
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Curve of Point"].outputs[0],
        spline_raycast_nodes_1.nodes["Sample Index.005"].inputs[1]
    )
    # sample_index_005.Value -> points_001.Radius
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Sample Index.005"].outputs[0],
        spline_raycast_nodes_1.nodes["Points.001"].inputs[2]
    )
    # index_003.Index -> sample_index_006.Index
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Index.003"].outputs[0],
        spline_raycast_nodes_1.nodes["Sample Index.006"].inputs[2]
    )
    # points.Points -> store_named_attribute_006.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Points"].outputs[0],
        spline_raycast_nodes_1.nodes["Store Named Attribute.006"].inputs[0]
    )
    # sample_curve.Value -> points.Radius
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Sample Curve"].outputs[0],
        spline_raycast_nodes_1.nodes["Points"].inputs[2]
    )
    # named_attribute_008.Attribute -> store_named_attribute_006.Value
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Named Attribute.008"].outputs[0],
        spline_raycast_nodes_1.nodes["Store Named Attribute.006"].inputs[3]
    )
    # named_attribute_009.Attribute -> sample_index_006.Value
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Named Attribute.009"].outputs[0],
        spline_raycast_nodes_1.nodes["Sample Index.006"].inputs[1]
    )
    # trim_curve_001.Curve -> domain_size_001.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Trim Curve.001"].outputs[0],
        spline_raycast_nodes_1.nodes["Domain Size.001"].inputs[0]
    )
    # trim_curve_001.Curve -> sample_index_003.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Trim Curve.001"].outputs[0],
        spline_raycast_nodes_1.nodes["Sample Index.003"].inputs[0]
    )
    # trim_curve_001.Curve -> sample_index_005.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Trim Curve.001"].outputs[0],
        spline_raycast_nodes_1.nodes["Sample Index.005"].inputs[0]
    )
    # curve_of_point.Index in Curve -> compare_002.A
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Curve of Point"].outputs[1],
        spline_raycast_nodes_1.nodes["Compare.002"].inputs[0]
    )
    # delete_geometry.Geometry -> sample_index_004.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Delete Geometry"].outputs[0],
        spline_raycast_nodes_1.nodes["Sample Index.004"].inputs[0]
    )
    # delete_geometry.Geometry -> sample_index_006.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Delete Geometry"].outputs[0],
        spline_raycast_nodes_1.nodes["Sample Index.006"].inputs[0]
    )
    # named_attribute_007.Attribute -> points_to_curves.Curve Group ID
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Named Attribute.007"].outputs[0],
        spline_raycast_nodes_1.nodes["Points to Curves"].inputs[1]
    )
    # sample_index_006.Value -> points_002.Radius
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Sample Index.006"].outputs[0],
        spline_raycast_nodes_1.nodes["Points.002"].inputs[2]
    )
    # points_002.Points -> join_geometry_002.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Points.002"].outputs[0],
        spline_raycast_nodes_1.nodes["Join Geometry.002"].inputs[0]
    )
    # join_geometry_002.Geometry -> points_to_curves.Points
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Join Geometry.002"].outputs[0],
        spline_raycast_nodes_1.nodes["Points to Curves"].inputs[0]
    )
    # realize_instances.Geometry -> sample_index_007.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Realize Instances"].outputs[0],
        spline_raycast_nodes_1.nodes["Sample Index.007"].inputs[0]
    )
    # index_004.Index -> sample_index_007.Index
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Index.004"].outputs[0],
        spline_raycast_nodes_1.nodes["Sample Index.007"].inputs[2]
    )
    # index_004.Index -> sample_index_007.Value
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Index.004"].outputs[0],
        spline_raycast_nodes_1.nodes["Sample Index.007"].inputs[1]
    )
    # curve_of_point_003.Curve Index -> sample_curve.Value
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Curve of Point.003"].outputs[0],
        spline_raycast_nodes_1.nodes["Sample Curve"].inputs[1]
    )
    # compare_007.Result -> switch.Switch
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Compare.007"].outputs[0],
        spline_raycast_nodes_1.nodes["Switch"].inputs[0]
    )
    # domain_size.Point Count -> compare_007.A
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Domain Size"].outputs[0],
        spline_raycast_nodes_1.nodes["Compare.007"].inputs[0]
    )
    # points_to_curves.Curves -> switch.True
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Points to Curves"].outputs[0],
        spline_raycast_nodes_1.nodes["Switch"].inputs[2]
    )
    # set_position_003.Geometry -> switch.False
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Set Position.003"].outputs[0],
        spline_raycast_nodes_1.nodes["Switch"].inputs[1]
    )
    # switch.Output -> join_geometry_001.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Switch"].outputs[0],
        spline_raycast_nodes_1.nodes["Join Geometry.001"].inputs[0]
    )
    # separate_components.Curve -> store_named_attribute_002.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Separate Components"].outputs[1],
        spline_raycast_nodes_1.nodes["Store Named Attribute.002"].inputs[0]
    )
    # separate_components.Curve -> sample_index.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Separate Components"].outputs[1],
        spline_raycast_nodes_1.nodes["Sample Index"].inputs[0]
    )
    # group_input.Geometry -> separate_components.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Group Input"].outputs[0],
        spline_raycast_nodes_1.nodes["Separate Components"].inputs[0]
    )
    # separate_components.Volume -> join_geometry_003.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Separate Components"].outputs[4],
        spline_raycast_nodes_1.nodes["Join Geometry.003"].inputs[0]
    )
    # join_geometry_003.Geometry -> join_geometry.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Join Geometry.003"].outputs[0],
        spline_raycast_nodes_1.nodes["Join Geometry"].inputs[0]
    )
    # store_named_attribute_005.Geometry -> join_geometry_002.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Store Named Attribute.005"].outputs[0],
        spline_raycast_nodes_1.nodes["Join Geometry.002"].inputs[0]
    )
    # separate_geometry_001.Inverted -> join_geometry.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Separate Geometry.001"].outputs[1],
        spline_raycast_nodes_1.nodes["Join Geometry"].inputs[0]
    )
    # separate_components.Instances -> join_geometry_003.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Separate Components"].outputs[5],
        spline_raycast_nodes_1.nodes["Join Geometry.003"].inputs[0]
    )
    # for_each_geometry_element_output.Geometry -> join_geometry.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["For Each Geometry Element Output"].outputs[2],
        spline_raycast_nodes_1.nodes["Join Geometry"].inputs[0]
    )
    # separate_components.Point Cloud -> join_geometry_003.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Separate Components"].outputs[3],
        spline_raycast_nodes_1.nodes["Join Geometry.003"].inputs[0]
    )
    # separate_components.Mesh -> join_geometry_003.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Separate Components"].outputs[0],
        spline_raycast_nodes_1.nodes["Join Geometry.003"].inputs[0]
    )
    # separate_components.Grease Pencil -> join_geometry_003.Geometry
    spline_raycast_nodes_1.links.new(
        spline_raycast_nodes_1.nodes["Separate Components"].outputs[2],
        spline_raycast_nodes_1.nodes["Join Geometry.003"].inputs[0]
    )

    return spline_raycast_nodes_1


if __name__ == "__main__":
    # Maps node tree creation functions to the node tree 
    # name, such that we don't recreate node trees unnecessarily
    node_tree_names : dict[typing.Callable, str] = {}

    spline_raycast_nodes = spline_raycast_nodes_1_node_group(node_tree_names)
    node_tree_names[spline_raycast_nodes_1_node_group] = spline_raycast_nodes.name

