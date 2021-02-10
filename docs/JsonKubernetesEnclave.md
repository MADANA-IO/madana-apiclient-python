# JsonKubernetesEnclave


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wireguard_server** | **str** |  | [optional] 
**signer_ident** | **str** |  | [optional] 
**ending_time** | **str** |  | [optional] 
**public_ident** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**console_output** | **str** |  | [optional] 
**startup_time** | **str** |  | [optional] 
**enclave_ident** | **str** |  | [optional] 
**process** | [**JsonProcess**](JsonProcess.md) |  | [optional] 
**internal_remote_control_server** | **str** |  | [optional] 
**attestation_server** | **str** |  | [optional] 
**remote_control_server** | **str** |  | [optional] 
**enclave_inputstream** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**internal_attesation_server** | **str** |  | [optional] 
**environment** | [**JsonEnvironment**](JsonEnvironment.md) |  | [optional] 
**wireguard_public_key** | **str** |  | [optional] 
**startup_cmd** | **str** |  | [optional] 
**wg_interface** | [**JsonWireguardInterface**](JsonWireguardInterface.md) |  | [optional] 
**internal_wireguard_server** | **str** |  | [optional] 
**port_mapping** | **{str: (str,)}** |  | [optional] 
**internal_ident** | **str** |  | [optional] 
**ports** | [**[JsonEnclavePort]**](JsonEnclavePort.md) |  | [optional] 
**kubernetes_enclave** | [**JsonKubernetesEnclave**](JsonKubernetesEnclave.md) |  | [optional] 
**debug_info** | **str** |  | [optional] 
**attestation_port** | **int** |  | [optional] 
**pod_phase** | **str** |  | [optional] 
**is_using_init_container** | **bool** |  | [optional] 
**enclave_pod_events** | [**JsonV1EventList**](JsonV1EventList.md) |  | [optional] 
**remote_control_ip** | **str** |  | [optional] 
**enclave_replica_set_events** | [**JsonV1EventList**](JsonV1EventList.md) |  | [optional] 
**enclave_deployment_events** | [**JsonV1EventList**](JsonV1EventList.md) |  | [optional] 
**wireguard_port** | **int** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


