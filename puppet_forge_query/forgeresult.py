from tabulate import tabulate


class ForgeResult:

    def module_description(result, latest):
        latest_version = result['current_release']['version']
        if latest:
            print(latest_version)
        else:
            name     = result['slug']
            url      = result['homepage_url']
            metadata = result['current_release']['metadata']
            print("*{}* ({})".format(name, url))
            print(metadata['summary'])

    def module_list(result, latest):
        headers = ["Module", "Name", "Latest version"]
        table   = []
        for module in result:
             table += [ [
                       module['slug'],
                       module['name'],
                       module['current_release']['version']
                      ] ]

        print(tabulate(table, headers))
