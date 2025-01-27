import numpy as np
import uuid
import hashlib


def export_traj(file_paths: dict,
                traj_race: np.ndarray):
    """
    Created by:
    Alexander Heilmeier

    Documentation:
    This function is used to export the generated trajectory into several files for further usage in the local
    trajectory planner on the car. The generated files get an unique UUID and a hash of the ggv diagram to be able to
    check it later.

    Inputs:
    file_paths:     paths for input and output files {ggv, traj_race_export, traj_ltpl_export, lts_export}
    traj_race:      race trajectory [s_m, x_m, y_m, psi_rad, kappa_radpm, vx_mps, ax_mps2]
    """

    # create random UUID
    rand_uuid = str(uuid.uuid4())

    # hash GGV file with SHA1
    with open(file_paths["ggv"], 'br') as fh:
        ggv_content = fh.read()
    ggv_hash = hashlib.sha1(ggv_content).hexdigest()

    # write UUID and GGV hash into file
    with open(file_paths["traj_race_export"], 'w') as fh:
        fh.write("# " + rand_uuid + "\n")
        fh.write("# " + ggv_hash + "\n")

    # export race trajectory
    header = "s_m; x_m; y_m; psi_rad; kappa_radpm; vx_mps; ax_mps2"
    fmt = "%.7f; %.7f; %.7f; %.7f; %.7f; %.7f; %.7f"
    with open(file_paths["traj_race_export"], 'ab') as fh:
        np.savetxt(fh, traj_race, fmt=fmt, header=header)


# testing --------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    pass
