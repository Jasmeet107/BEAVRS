import h5py
import numpy

assembly_names = ['pwru160c00','pwru240c00','pwru240w12','pwru310c00','pwru310w12']
group_types =['2-group/','8-group/']
write_file = h5py.File('averaged-xs-data.hdf5')
for name in assembly_names:
    assembly_group = write_file.create_group(name)
    for group in group_types:
        energy_group = write_file.create_group(group.strip('/'))
        read_file = h5py.File('casmo-data/'+group+name+'-materials.hdf5','r')

        microregion_lower_bound = 0
        microregion_upper_bound = 0
        string_pin_cell_array = numpy.zeros((17,17))

        for i in range(len(string_pin_cell_array)):
            for j in range(len(string_pin_cell_array[i])):


                #create empty arrays for XS data
                fission_avgs = numpy.zeros(string_pin_cell_array.shape())
                absorption_avgs = numpy.zeros(string_pin_cell_array.shape())
                diffusion_avgs = numpy.zeros(string_pin_cell_array.shape())
                nu_fission_avgs = numpy.zeros(string_pin_cell_array.shape())
                scatter_avgs = numpy.zeros(string_pin_cell_array.shape())

                num_energy_groups = f['Energy Groups']
                if string_pin_cell_array[i][j]=='gt':
                    microregion_upper_bound = microregion_lower_bound+4
                elif string_pin_cell_array[i][j]=='fuel':
                    microregion_upper_bound = microregion_lower_bound+7
                elif string_pin_cell_array[i][j]=='bp':
                    microregion_upper_bound = microregion_lower_bound+7

                fission_avgs[i][j] = sum([sum(f['microregion-'+microregion]['Fission XS'])/(num_energy_groups*(microregion_upper_bound-microregion_lower_bound-1)) for microregion in range(microregion_lower_bound,microregion_upper_bound)])

                microregion_lower_bound = microregion_upper_bound
                    
                
