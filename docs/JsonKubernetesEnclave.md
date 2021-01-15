# JsonKubernetesEnclave


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wg_interface** | [**JsonWireguardInterface**](JsonWireguardInterface.md) |  | [optional] 
**environment** | [**JsonEnvironment**](JsonEnvironment.md) |  | [optional] 
**startup_cmd** | **str** |  | [optional] 
**internal_remote_control_server** | **str** |  | [optional] 
**console_output** | **str** |  | [optional] 
**ending_time** | **str** |  | [optional] 
**startup_time** | **str** |  | [optional] 
**remote_control_server** | **str** |  | [optional] 
**ports** | [**[JsonEnclavePort]**](JsonEnclavePort.md) |  | [optional] 
**kubernetes_enclave** | [**JsonKubernetesEnclave**](JsonKubernetesEnclave.md) |  | [optional] 
**wireguard_server** | **str** |  | [optional] 
**internal_wireguard_server** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**wireguard_public_key** | **str** |  | [optional] 
**enclave_ident** | **str** |  | [optional] 
**internal_ident** | **str** |  | [optional] 
**public_ident** | **str** |  | [optional] 
**process** | [**JsonProcess**](JsonProcess.md) |  | [optional] 
**internal_attesation_server** | **str** |  | [optional] 
**signer_ident** | **str** |  | [optional] 
**enclave_inputstream** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**attestation_server** | **str** |  | [optional] 
**port_mapping** | **{str: (str,)}** |  | [optional] 
**enclave_replica_set_events** | [**JsonV1EventList**](JsonV1EventList.md) |  | [optional] 
**wireguard_port** | **int** |  | [optional] 
**attestation_port** | **int** |  | [optional] 
**enclave_deployment_events** | [**JsonV1EventList**](JsonV1EventList.md) |  | [optional] 
**enclave_pod_events** | [**JsonV1EventList**](JsonV1EventList.md) |  | [optional] 
**is_using_init_container** | **bool** |  | [optional] 
**pod_phase** | **str** |  | [optional] 
**debug_info** | **str** |  | [optional] 
**remote_control_ip** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


