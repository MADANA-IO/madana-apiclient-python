# JsonKubernetesEnclave


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**startup_time** | **str** |  | [optional] 
**environment** | [**JsonEnvironment**](JsonEnvironment.md) |  | [optional] 
**enclave_ident** | **str** |  | [optional] 
**wireguard_server** | **str** |  | [optional] 
**ports** | [**[JsonEnclavePort]**](JsonEnclavePort.md) |  | [optional] 
**enclave_inputstream** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**signer_ident** | **str** |  | [optional] 
**ending_time** | **str** |  | [optional] 
**internal_remote_control_server** | **str** |  | [optional] 
**attestation_server** | **str** |  | [optional] 
**console_output** | **str** |  | [optional] 
**internal_ident** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**kubernetes_enclave** | [**JsonKubernetesEnclave**](JsonKubernetesEnclave.md) |  | [optional] 
**internal_attesation_server** | **str** |  | [optional] 
**startup_cmd** | **str** |  | [optional] 
**port_mapping** | **{str: (str,)}** |  | [optional] 
**process** | [**JsonProcess**](JsonProcess.md) |  | [optional] 
**wireguard_public_key** | **str** |  | [optional] 
**remote_control_server** | **str** |  | [optional] 
**wg_interface** | [**JsonWireguardInterface**](JsonWireguardInterface.md) |  | [optional] 
**internal_wireguard_server** | **str** |  | [optional] 
**public_ident** | **str** |  | [optional] 
**enclave_replica_set_events** | [**JsonV1EventList**](JsonV1EventList.md) |  | [optional] 
**is_using_init_container** | **bool** |  | [optional] 
**attestation_port** | **int** |  | [optional] 
**wireguard_port** | **int** |  | [optional] 
**pod_phase** | **str** |  | [optional] 
**enclave_pod_events** | [**JsonV1EventList**](JsonV1EventList.md) |  | [optional] 
**enclave_deployment_events** | [**JsonV1EventList**](JsonV1EventList.md) |  | [optional] 
**remote_control_ip** | **str** |  | [optional] 
**debug_info** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


