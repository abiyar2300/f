def validate_source_paths(source_paths : List[str]) -> Tuple[List[str], List[str]]:
    valid_source_paths = []
    invalid_source_paths = []

    for source_path in source_paths:
        if validate_hash(source_path):
            valid_source_paths.append(source_path)
        else:
            invalid_source_paths.append(source_path)

    return valid_source_paths, invalid_source_paths

