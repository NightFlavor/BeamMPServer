import toml

def get_map_selection():
    maps = {
        "westcoast": "west_coast_usa",
        "eastcoast": "east_coast_usa",
        "italy": "italy",
        "junglerock": "jungle_rock_island",
        "industrial": "industrial",
        "utah": "utah",
        "derby": "derby",
        "johnson": "johnson_valley",
        "automation": "automation_test_track",
        "hirochi": "hirochi_raceway",
        "gridmap": "GridMap",
        "gridmapv2": "gridmap_v2"
    }

    print("Available maps:")
    for key in maps.keys():
        print(f"- {key}")

    chosen_map_name = input("Enter the map you want: ").strip().lower()

    if chosen_map_name not in maps:
        print("Invalid map name entered.")
        return None

    return f"levels/{maps[chosen_map_name]}/info.json"

def update_server_config(file_path, map_path):
    try:
        with open(file_path, 'r') as file:
            server_config = toml.load(file)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")
        return

    server_config['General']['Map'] = map_path

    try:
        with open(file_path, 'w') as file:
            toml.dump(server_config, file)
        print(f"Map successfully updated to {map_path}")
    except IOError as e:
        print(f"Error writing to file {file_path}: {e}")

def main():
    config_file_path = "ServerConfig.toml"
    new_map_path = get_map_selection()

    if new_map_path:
        update_server_config(config_file_path, new_map_path)

if __name__ == "__main__":
    main()
