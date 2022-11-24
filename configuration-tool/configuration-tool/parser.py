from sys import argv
import json


def insert(value, key):
    sim_function = {
        "sim_function": {
            "name": value["similarity"],
            "params": [],
            "on_attribute": {
                "att_name": key,
                "att_type": value["type"]
            },
            "interaction_object": {
                "att_name": "artworkId",
                "att_type": "String"
            }
        }
    }
    return sim_function


if __name__ == "__main__":
    route = "configFile.json"

    f = open(route)
    data = json.load(f)
    lista_artworks = []
    # artworkAttributesFilter = ["Artwork_Artistic_Movement", "Artwork_start_date", "Artist_birth_data", "Artwork_type", "Author",
    #                            "Collection", "Gender", "Materials", "Size_height", "Size_width", "Technique", "Artist_country", "Iconclass_subjects_curators",
    #                            "Author", "Year", "Size_height", "Size_width", "Inventary"]
    for key in data["artworks"]:
        value = data["artworks"][key]
        sim_function = {
            "sim_function": {
                "name": value["similarity"],
                "params": [],
                "on_attribute": {
                    "att_name": key,
                    "att_type": value["type"]
                }
            }
        }
        lista_artworks.append(sim_function)

    lista_interactions = []
    for key in data["interactions"]:
        value = data["interactions"][key]
        if key in ["emotions", "sentiments"]:
            sim_function = insert(value, key)
            lista_interactions.append(sim_function)
        else:
            pass
        # if key == "multimediaData":
        #     for i in value:
        #         for j in value[i]:
        #             sim_function = insert(value[i][j], j)
        #             lista_interactions.append(sim_function)
        # else:
        #     sim_function = insert(value, key)
        #     lista_interactions.append(sim_function)

    config = {
        "artwork_attributes": lista_artworks,
        "user_attributes": [
            {
                "att_name": "Age",
                "att_type": "String"
            },
            {
                "att_name": "Gender",
                "att_type": "String"
            },
            {
                "att_name": "relationship_with_arts",
                "att_type": "String"
            },
            {
                "att_name": "relationship_with_museums",
                "att_type": "String"
            },
            {
                "att_name": "content_breaking",
                "att_type": "String"
            }],
        "interaction_similarity_functions": lista_interactions
    }

    outfileName = route.replace('.json', '')
    outfileName = outfileName + "_ParsedOutput.json"
    with open(outfileName, "w") as outfile:
        outfile.write(json.dumps(config, indent=4))
