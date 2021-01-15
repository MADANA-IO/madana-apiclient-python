# JsonKubernetesEnclave


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ports** | [**[JsonEnclavePort]**](JsonEnclavePort.md) |  | [optional] 
**public_ident** | **str** |  | [optional] 
**console_output** | **str** |  | [optional] 
**wireguard_server** | **str** |  | [optional] 
**process** | [**JsonProcess**](JsonProcess.md) |  | [optional] 
**internal_attesation_server** | **str** |  | [optional] 
**startup_time** | **str** |  | [optional] 
**attestation_server** | **str** |  | [optional] 
**port_mapping** | **{str: (str,)}** |  | [optional] 
**wg_interface** | [**JsonWireguardInterface**](JsonWireguardInterface.md) |  | [optional] 
**kubernetes_enclave** | [**JsonKubernetesEnclave**](JsonKubernetesEnclave.md) |  | [optional] 
**ending_time** | **str** |  | [optional] 
**internal_wireguard_server** | **str** |  | [optional] 
**wireguard_public_key** | **str** |  | [optional] 
**signer_ident** | **str** |  | [optional] 
**internal_remote_control_server** | **str** |  | [optional] 
**enclave_ident** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**startup_cmd** | **str** |  | [optional] 
**internal_ident** | **str** |  | [optional] 
**environment** | [**JsonEnvironment**](JsonEnvironment.md) |  | [optional] 
**enclave_inputstream** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**remote_control_server** | **str** |  | [optional] 
**enclave_deployment_events** | [**JsonV1EventList**](JsonV1EventList.md) |  | [optional] 
**attestation_port** | **int** |  | [optional] 
**wireguard_port** | **int** |  | [optional] 
**pod_phase** | **str** |  | [optional] 
**enclave_replica_set_events** | [**JsonV1EventList**](JsonV1EventList.md) |  | [optional] 
**debug_info** | **str** |  | [optional] 
**enclave_pod_events** | [**JsonV1EventList**](JsonV1EventList.md) |  | [optional] 
**is_using_init_container** | **bool** |  | [optional] 
**remote_control_ip** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


