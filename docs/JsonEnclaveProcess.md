# JsonEnclaveProcess


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_ident** | **str** |  | [optional] 
**enclave_ident** | **str** |  | [optional] 
**enclave_inputstream** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**kubernetes_enclave** | [**JsonKubernetesEnclave**](JsonKubernetesEnclave.md) |  | [optional] 
**port_mapping** | **{str: (str,)}** |  | [optional] 
**status** | **str** |  | [optional] 
**startup_cmd** | **str** |  | [optional] 
**process** | [**JsonProcess**](JsonProcess.md) |  | [optional] 
**console_output** | **str** |  | [optional] 
**ending_time** | **str** |  | [optional] 
**signer_ident** | **str** |  | [optional] 
**remote_control_server** | **str** |  | [optional] 
**internal_ident** | **str** |  | [optional] 
**internal_remote_control_server** | **str** |  | [optional] 
**wg_interface** | [**JsonWireguardInterface**](JsonWireguardInterface.md) |  | [optional] 
**attestation_server** | **str** |  | [optional] 
**startup_time** | **str** |  | [optional] 
**environment** | [**JsonEnvironment**](JsonEnvironment.md) |  | [optional] 
**internal_wireguard_server** | **str** |  | [optional] 
**wireguard_public_key** | **str** |  | [optional] 
**internal_attesation_server** | **str** |  | [optional] 
**ports** | [**[JsonEnclavePort]**](JsonEnclavePort.md) |  | [optional] 
**wireguard_server** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


