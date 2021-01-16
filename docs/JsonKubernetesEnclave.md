# JsonKubernetesEnclave


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_ident** | **str** |  | [optional] 
**internal_ident** | **str** |  | [optional] 
**internal_attesation_server** | **str** |  | [optional] 
**ports** | [**[JsonEnclavePort]**](JsonEnclavePort.md) |  | [optional] 
**startup_time** | **str** |  | [optional] 
**kubernetes_enclave** | [**JsonKubernetesEnclave**](JsonKubernetesEnclave.md) |  | [optional] 
**status** | **str** |  | [optional] 
**port_mapping** | **{str: (str,)}** |  | [optional] 
**remote_control_server** | **str** |  | [optional] 
**wg_interface** | [**JsonWireguardInterface**](JsonWireguardInterface.md) |  | [optional] 
**internal_remote_control_server** | **str** |  | [optional] 
**wireguard_server** | **str** |  | [optional] 
**internal_wireguard_server** | **str** |  | [optional] 
**enclave_inputstream** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**startup_cmd** | **str** |  | [optional] 
**environment** | [**JsonEnvironment**](JsonEnvironment.md) |  | [optional] 
**attestation_server** | **str** |  | [optional] 
**console_output** | **str** |  | [optional] 
**wireguard_public_key** | **str** |  | [optional] 
**enclave_ident** | **str** |  | [optional] 
**ending_time** | **str** |  | [optional] 
**process** | [**JsonProcess**](JsonProcess.md) |  | [optional] 
**signer_ident** | **str** |  | [optional] 
**pod_phase** | **str** |  | [optional] 
**enclave_deployment_events** | [**JsonV1EventList**](JsonV1EventList.md) |  | [optional] 
**is_using_init_container** | **bool** |  | [optional] 
**enclave_replica_set_events** | [**JsonV1EventList**](JsonV1EventList.md) |  | [optional] 
**wireguard_port** | **int** |  | [optional] 
**enclave_pod_events** | [**JsonV1EventList**](JsonV1EventList.md) |  | [optional] 
**remote_control_ip** | **str** |  | [optional] 
**debug_info** | **str** |  | [optional] 
**attestation_port** | **int** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


