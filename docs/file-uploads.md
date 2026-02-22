# File uploads

File uploads (designs and images) use a specific flow on the Thingiverse API.

## Official guide

See the [Thingiverse upload guide](https://www.thingiverse.com/developers/upload-guide) for the full flow, including:

- The single upload entry point: `/files/0/uploadFile`
- Finalizing uploads: `/files/0/FinalizeFiles`
- How the backend routes content by type (images vs other files)

## Using the SDK

Once the client is generated from the full OpenAPI spec (including the file resource), you will have:

- Generated methods for the upload and finalize endpoints
- Optionally a thin hand-written helper that wraps the upload-then-finalize flow

Use the generated API modules under `thingiverse_client.api` for `uploadFile` and `FinalizeFiles`; refer to the upload guide for request format and ordering.
