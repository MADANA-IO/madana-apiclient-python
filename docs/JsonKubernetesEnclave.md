# JsonKubernetesEnclave


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enclave_ident** | **str** |  | [optional] 
**port_mapping** | **{str: (str,)}** |  | [optional] 
**wireguard_public_key** | **str** |  | [optional] 
**signer_ident** | **str** |  | [optional] 
**internal_ident** | **str** |  | [optional] 
**internal_remote_control_server** | **str** |  | [optional] 
**ports** | [**[JsonEnclavePort]**](JsonEnclavePort.md) |  | [optional] 
**public_ident** | **str** |  | [optional] 
**enclave_inputstream** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**kubernetes_enclave** | [**JsonKubernetesEnclave**](JsonKubernetesEnclave.md) |  | [optional] 
**internal_wireguard_server** | **str** |  | [optional] 
**internal_attesation_server** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**wg_interface** | [**JsonWireguardInterface**](JsonWireguardInterface.md) |  | [optional] 
**console_output** | **str** |  | [optional] 
**remote_control_server** | **str** |  | [optional] 
**startup_cmd** | **str** |  | [optional] 
**attestation_server** | **str** |  | [optional] 
**ending_time** | **str** |  | [optional] 
**process** | [**JsonProcess**](JsonProcess.md) |  | [optional] 
**startup_time** | **str** |  | [optional] 
**environment** | [**JsonEnvironment**](JsonEnvironment.md) |  | [optional] 
**wireguard_server** | **str** |  | [optional] 
**wireguard_port** | **int** |  | [optional] 
**debug_info** | **str** |  | [optional] 
**is_using_init_container** | **bool** |  | [optional] 
**enclave_pod_events** | [**JsonV1EventList**](JsonV1EventList.md) |  | [optional] 
**pod_phase** | **str** |  | [optional] 
**remote_control_ip** | **str** |  | [optional] 
**enclave_replica_set_events** | [**JsonV1EventList**](JsonV1EventList.md) |  | [optional] 
**attestation_port** | **int** |  | [optional] 
**enclave_deployment_events** | [**JsonV1EventList**](JsonV1EventList.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


