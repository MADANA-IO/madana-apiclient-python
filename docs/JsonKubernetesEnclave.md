# JsonKubernetesEnclave


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_wireguard_server** | **str** |  | [optional] 
**public_ident** | **str** |  | [optional] 
**wireguard_public_key** | **str** |  | [optional] 
**process** | [**JsonProcess**](JsonProcess.md) |  | [optional] 
**port_mapping** | **{str: (str,)}** |  | [optional] 
**internal_remote_control_server** | **str** |  | [optional] 
**remote_control_server** | **str** |  | [optional] 
**attestation_server** | **str** |  | [optional] 
**signer_ident** | **str** |  | [optional] 
**wg_interface** | [**JsonWireguardInterface**](JsonWireguardInterface.md) |  | [optional] 
**startup_time** | **str** |  | [optional] 
**ending_time** | **str** |  | [optional] 
**enclave_inputstream** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**internal_ident** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**kubernetes_enclave** | [**JsonKubernetesEnclave**](JsonKubernetesEnclave.md) |  | [optional] 
**enclave_ident** | **str** |  | [optional] 
**startup_cmd** | **str** |  | [optional] 
**wireguard_server** | **str** |  | [optional] 
**ports** | [**[JsonEnclavePort]**](JsonEnclavePort.md) |  | [optional] 
**internal_attesation_server** | **str** |  | [optional] 
**console_output** | **str** |  | [optional] 
**environment** | [**JsonEnvironment**](JsonEnvironment.md) |  | [optional] 
**attestation_port** | **int** |  | [optional] 
**is_using_init_container** | **bool** |  | [optional] 
**enclave_deployment_events** | [**JsonV1EventList**](JsonV1EventList.md) |  | [optional] 
**debug_info** | **str** |  | [optional] 
**remote_control_ip** | **str** |  | [optional] 
**enclave_pod_events** | [**JsonV1EventList**](JsonV1EventList.md) |  | [optional] 
**enclave_replica_set_events** | [**JsonV1EventList**](JsonV1EventList.md) |  | [optional] 
**pod_phase** | **str** |  | [optional] 
**wireguard_port** | **int** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


