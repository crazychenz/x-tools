## Synposis

- List pre-configured toolchains: `./list.sh`
- Stage a new configuration: `./stage.sh <target> <alias>`
- Create a configuration: `./config.sh <alias>`
- Build configuration: `./build.sh <alias>`

## Example

```sh
# Find x86_64 builds.
./list.sh | grep x86_64

# Stage an x86_64 build as 'x86_64-static_multilib-linux-gnu'.
./stage.sh x86_64-multilib-linux-gnu x86_64-static_multilib-linux-gnu

# Configure 'x86_64-static_multilib-linux-gnu' vendor and static settings.
./config.sh x86_64-static_multilib-linux-gnu

# Build 'x86_64-static_multilib-linux-gnu'.
./build.sh x86_64-static_multilib-linux-gnu
```